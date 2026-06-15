from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app import CustomerCareChatbot

app = FastAPI(title="Thredd Cards API Documentation Assistant")

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot (singleton for app lifetime).
# force_rebuild=False so startup loads the cached scrape + FAISS index instead of
# re-scraping ~150 pages on every boot. The first-ever boot (no cache) scrapes once.
chatbot = CustomerCareChatbot(force_rebuild=False)


class QueryRequest(BaseModel):
    question: str
    session_id: str = "default"


@app.post("/query")
async def query_chatbot(request: QueryRequest):
    response = chatbot.query(request.question, request.session_id)
    return {"answer": response}


@app.post("/refresh")
async def refresh_documents(background_tasks: BackgroundTasks):
    # Re-scraping the docs can take ~1-2 minutes; run it in the background.
    background_tasks.add_task(chatbot.refresh_knowledge_base)
    return {"status": "Documentation refresh started. This may take a couple of minutes."}


@app.get("/documents")
async def list_documents():
    metadata = chatbot.load_metadata()
    pages = metadata.get("pages", {}) if isinstance(metadata, dict) else {}
    docs = []
    for url, info in pages.items():
        docs.append({
            "title": info.get("title"),
            "url": url,
            "section": info.get("section"),
            "fetched_at": info.get("fetched_at"),
        })
    return {"documents": docs, "count": len(docs)}


@app.get("/scrape-status")
async def scrape_status():
    metadata = chatbot.load_metadata()
    if not isinstance(metadata, dict) or not metadata.get("pages"):
        return {"scraped": False}
    return {
        "scraped": True,
        "scraped_at": metadata.get("scraped_at"),
        "base_url": metadata.get("base_url"),
        "page_count": len(metadata.get("pages", {})),
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
