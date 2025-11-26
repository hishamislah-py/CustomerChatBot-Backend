from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app import CustomerCareChatbot
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot (singleton for app lifetime)
# Force rebuild to avoid pickle compatibility issues between environments
chatbot = CustomerCareChatbot(force_rebuild=True)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_chatbot(request: QueryRequest):
    response = chatbot.query(request.question)
    return {"answer": response}

@app.post("/refresh")
async def refresh_documents():
    chatbot.refresh_documents()
    return {"status": "Document index refreshed!"}

@app.get("/documents")
async def list_documents():
    metadata = chatbot.load_metadata()
    if not metadata:
        return {"documents": []}
    docs = []
    for filename, info in metadata.items():
        docs.append({
            "filename": filename,
            "path": info["path"],
            "last_modified": info["last_modified"]
        })
    return {"documents": docs}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}