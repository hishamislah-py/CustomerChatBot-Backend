import os
import glob
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from scraper import ThreddDocsScraper
import pickle
import hashlib
import json
from pathlib import Path
from typing import Dict

# Load environment variables
load_dotenv()

class CustomerCareChatbot:
    def __init__(self, data_folder="data", force_rebuild=False):
        self.data_folder = data_folder
        # Knowledge base is now scraped from the Thredd Cards API docs; the scraper owns
        # this manifest (web analogue of the old document_metadata.json).
        self.metadata_file = "scrape_manifest.json"
        self.scraper = ThreddDocsScraper()

        # Initialize memory store for different sessions
        self.store: Dict[str, BaseChatMessageHistory] = {}

        # Initialize components
        self.initialize_components()
        
        # Process documents and create vector store
        self.process_documents(force_rebuild)
        
        # Setup the retrieval chain with memory
        self.setup_retrieval_chain_with_memory()
    
    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        """Get or create chat history for a session"""
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]
    
    def initialize_components(self):
        """Initialize all necessary components"""
        # Initialize Groq LLM
        self.llm = ChatGroq(
            temperature=0.3,
            model_name="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        # Initialize embedding model (free HuggingFace model)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # FAISS vector store path + a signature of the corpus it was built from.
        # The signature lets us detect a stale/foreign index (e.g. one left over from
        # the old PDF data) and rebuild it instead of silently serving stale answers.
        self.faiss_index_path = "faiss_index"
        self.faiss_signature_path = "faiss_index.sig"

    def _corpus_signature(self, documents):
        """Stable hash of the full document corpus, used to validate the FAISS index."""
        h = hashlib.md5()
        for content in sorted(d.page_content for d in documents):
            h.update(content.encode("utf-8"))
        return h.hexdigest()

    def get_file_hash(self, filepath):
        """Calculate MD5 hash of a file to detect changes"""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def load_metadata(self):
        """Load document metadata for change detection"""
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_metadata(self, metadata):
        """Save document metadata"""
        with open(self.metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def get_supported_files(self):
        """Get all supported files from the data folder"""
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            print(f"Created {self.data_folder} folder. Please add your customer care knowledge base documents there.")
            return []
        
        # Get all PDF and Word files
        pdf_files = glob.glob(os.path.join(self.data_folder, "*.pdf"))
        docx_files = glob.glob(os.path.join(self.data_folder, "*.docx"))
        doc_files = glob.glob(os.path.join(self.data_folder, "*.doc"))
        
        all_files = pdf_files + docx_files + doc_files
        print(f"Found {len(all_files)} customer care knowledge base documents:")
        for file in all_files:
            print(f"  - {os.path.basename(file)}")
        
        return all_files
    
    def check_for_changes(self, files):
        """Check if any files have changed since last processing"""
        current_metadata = self.load_metadata()
        
        # Check for new or modified files
        changes_detected = False
        new_metadata = {}
        
        for file_path in files:
            file_hash = self.get_file_hash(file_path)
            file_name = os.path.basename(file_path)
            new_metadata[file_name] = {
                'path': file_path,
                'hash': file_hash,
                'last_modified': os.path.getmtime(file_path)
            }
            
            if (file_name not in current_metadata or 
                current_metadata[file_name]['hash'] != file_hash):
                changes_detected = True
                print(f"Changes detected in: {file_name}")
        
        # Check for deleted files
        for old_file in current_metadata:
            if old_file not in new_metadata:
                changes_detected = True
                print(f"File removed: {old_file}")
        
        return changes_detected, new_metadata
    
    def load_document(self, file_path):
        """Load a document based on its file extension"""
        file_extension = Path(file_path).suffix.lower()
        
        try:
            if file_extension == '.pdf':
                loader = PyPDFLoader(file_path)
            elif file_extension in ['.docx', '.doc']:
                loader = Docx2txtLoader(file_path)
            else:
                print(f"Unsupported file type: {file_extension}")
                return []
            
            documents = loader.load()
            
            # Add source metadata to each document
            for doc in documents:
                doc.metadata['source_file'] = os.path.basename(file_path)
                doc.metadata['file_type'] = file_extension
            
            print(f"Loaded {len(documents)} pages from {os.path.basename(file_path)}")
            return documents
            
        except Exception as e:
            print(f"Error loading {file_path}: {str(e)}")
            return []
    
    def load_web_documents(self, force_rebuild=False):
        """Scrape the Thredd Cards API docs. Returns (documents, changed)."""
        return self.scraper.scrape_all(force=force_rebuild)

    def process_documents(self, force_rebuild=False):
        """Scrape the Thredd Cards API documentation and (re)build the vector store."""
        print("Loading Thredd Cards API documentation...")
        all_documents, changes_detected = self.load_web_documents(force_rebuild)

        if not all_documents:
            print("No documentation pages were loaded.")
            print("Check network access to https://cardsapidocs.thredd.com")
            return

        # Signature of the current corpus; only reuse a FAISS index that matches it.
        current_signature = self._corpus_signature(all_documents)
        existing_signature = None
        if os.path.exists(self.faiss_signature_path):
            with open(self.faiss_signature_path, "r", encoding="utf-8") as f:
                existing_signature = f.read().strip()

        # Reuse the existing FAISS index only when it was built from this exact corpus.
        if (os.path.exists(self.faiss_index_path) and
                not force_rebuild and
                not changes_detected and
                existing_signature == current_signature):
            print("Loading existing FAISS index (no changes detected)...")
            self.vectorstore = FAISS.load_local(
                self.faiss_index_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            return

        print(f"Building FAISS index from {len(all_documents)} documentation pages...")

        # Split documents into chunks (markdown splits cleanly on these separators).
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            separators=["\n\n", "\n", "•", ".", "?", "!", ";", ",", " "]
        )
        self.docs = text_splitter.split_documents(all_documents)
        print(f"Split documentation into {len(self.docs)} chunks")

        # Create and persist the FAISS vector store.
        self.vectorstore = FAISS.from_documents(
            self.docs,
            self.embeddings
        )
        self.vectorstore.save_local(self.faiss_index_path)
        with open(self.faiss_signature_path, "w", encoding="utf-8") as f:
            f.write(current_signature)

        print(f"FAISS index saved to {self.faiss_index_path}")
        print(f"Processed {len(all_documents)} documentation pages into {len(self.docs)} chunks")
    
    def setup_retrieval_chain_with_memory(self):
        """Setup the RAG retrieval chain with conversation memory for customer care queries"""
        if not hasattr(self, 'vectorstore'):
            print("No vector store available. Please ensure customer care documents are processed first.")
            return

        # Create retriever with more relevant documents for customer care
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 6}  # Increased for better customer care context
        )

        # Contextualize question prompt for the Thredd Cards API docs
        contextualize_q_system_prompt = """Given a chat history and the latest user question
        about the Thredd Cards API (cards, cardholders, 3D Secure, card controls,
        tokenisation, transactions, API endpoints, fields, error codes, integration, etc.),
        formulate a standalone question which can be understood without the chat history.

        IMPORTANT: For simple greetings like "Hi", "Hello", "Good morning", "Thank you", etc.,
        return them exactly as they are without any modification or context from chat history.

        For complex technical questions, reformulate them if needed to be standalone.
        Do NOT answer the question, just reformulate it if needed and otherwise return it as is."""

        contextualize_q_prompt = ChatPromptTemplate.from_messages([
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])

        # Create history-aware retriever
        history_aware_retriever = create_history_aware_retriever(
            self.llm, retriever, contextualize_q_prompt
        )

        # Thredd Cards API documentation assistant prompt
        qa_system_prompt = """You are the Thredd Cards API Documentation Assistant.
        You help developers and integration teams by answering questions strictly from the
        official Thredd Cards API documentation (https://cardsapidocs.thredd.com). Topics include:

        💳 Cards & Cardholders: creating, retrieving, updating, replacing, renewing cards; PINs, CVV, card status
        🔐 Security: 3D Secure enrolment, mTLS authentication, sending secure data
        🎛️ Card Controls & Limits: control groups, card limits, balances
        🔁 Tokenisation: payment tokens, binding/unbinding, card images
        🌐 API Reference: endpoints, request/response fields, parameters, status/error codes
        🧩 Integration: getting started, accessing the API, products and services

        STRICT SCOPE — READ THIS FIRST:
        You are NOT a general-purpose assistant. You answer ONLY using the Thredd Cards API
        documentation provided in the context below. You must NOT use any outside knowledge,
        general world knowledge, or training data to answer.
        - If a question is about anything other than the Thredd Cards API (e.g. people, history,
          geography, politics, general trivia, other companies/products, coding help unrelated
          to the Thredd Cards API, opinions, current events), you MUST refuse — even if you
          know the answer. Do NOT explain, guess, or offer alternatives about the off-topic subject.
        - If a question is on-topic but the answer is not in the provided context, say you
          couldn't find it in the documentation.
        - Never invent endpoints, fields, parameters, or behaviour that is not in the context.

        Response Guidelines:

        1. **For Greetings & Pleasantries** ("Hi", "Hello", "Good morning", "Thank you"):
           - Treat each greeting as a fresh interaction
           - Respond: "Hello! I'm the Thredd Cards API documentation assistant. Ask me anything about the Cards API — cards, 3D Secure, tokenisation, endpoints, fields, and more. How can I help?"
           - Do NOT reference previous conversations or say "again" or "still here"

        2. **For Off-Topic / Out-of-Scope Questions** (anything not about the Thredd Cards API):
           - Do NOT answer from general knowledge. Do NOT speculate about who/what the subject might be.
           - Reply ONLY with: "I can only help with questions about the Thredd Cards API. I don't have anything about that. Try asking about cards, cardholders, 3D Secure, card controls, tokenisation, or the API endpoints."
           - Do not add any extra information about the off-topic subject.

        3. **For On-Topic Technical Questions**:
           - Give accurate, developer-focused answers grounded ONLY in the documentation context
           - Use **bold headings**, numbered steps, and bullet points where helpful
           - Include endpoint paths, HTTP methods, request/response field names, and example values when present in the context
           - Preserve code, JSON, and tables from the documentation
           - Be as detailed as the question requires (do not artificially truncate technical answers)

        4. **Always Cite Sources** (for on-topic answers drawn from the context):
           - End the answer with a "Sources:" line listing the page title(s) and URL(s) from the context, e.g.
             "Sources: Introduction to 3D Secure (https://cardsapidocs.thredd.com/docs/introduction-to-3d-secure)"

        5. **If On-Topic But Not in the Documentation**:
           - Respond: "I couldn't find that in the Thredd Cards API documentation. Please check https://cardsapidocs.thredd.com or contact Thredd support."

        6. **Tone**: Professional, precise, and helpful — like good developer documentation.

        Context from the Thredd Cards API documentation:
        {context}"""

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])

        # Prefix each retrieved chunk with its source so the LLM can cite it.
        document_prompt = PromptTemplate.from_template(
            "Source: {title} ({source_url})\n{page_content}"
        )

        # Create the question-answer chain
        question_answer_chain = create_stuff_documents_chain(
            self.llm, qa_prompt, document_prompt=document_prompt
        )

        # Create the RAG chain with history awareness
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        # Wrap with message history
        self.conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            self.get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )
    
    def query(self, question, session_id="default"):
        """Query the Thredd Cards API documentation assistant with memory"""
        if not hasattr(self, 'conversational_rag_chain'):
            return "Sorry, the assistant is not properly initialized. Please ensure the documentation has been scraped successfully."

        try:
            response = self.conversational_rag_chain.invoke(
                {"input": question},
                config={"configurable": {"session_id": session_id}}
            )
            return response["answer"]
        except Exception as e:
            return f"I apologize, but I encountered an error while processing your request: {str(e)}. Please try again, or see https://cardsapidocs.thredd.com."
    
    def clear_memory(self, session_id="default"):
        """Clear conversation memory for a specific session"""
        if session_id in self.store:
            self.store[session_id].clear()
            print(f"Conversation history cleared for session: {session_id}")
        else:
            print(f"No conversation history found for session: {session_id}")
    
    def get_conversation_history(self, session_id="default"):
        """Get conversation history for a specific session"""
        if session_id in self.store:
            messages = self.store[session_id].messages
            if messages:
                print(f"\nConversation History for session '{session_id}':")
                print("-" * 60)
                for i, message in enumerate(messages, 1):
                    if isinstance(message, HumanMessage):
                        print(f"{i}. You: {message.content}")
                    elif isinstance(message, AIMessage):
                        print(f"{i}. Customer Care Assistant: {message.content[:150]}{'...' if len(message.content) > 150 else ''}")
                    print()
            else:
                print(f"No conversation history for session: {session_id}")
        else:
            print(f"No session found: {session_id}")
    
    def list_sessions(self):
        """List all active sessions"""
        if self.store:
            print("\nActive Client Sessions:")
            print("-" * 40)
            for session_id, history in self.store.items():
                message_count = len(history.messages)
                print(f"Session: {session_id} ({message_count} messages)")
        else:
            print("No active client sessions found.")
    
    def refresh_knowledge_base(self):
        """Manually refresh the customer care knowledge base"""
        print("Refreshing customer care knowledge base...")
        self.process_documents(force_rebuild=True)
        self.setup_retrieval_chain_with_memory()
        # Clear all conversation memories when refreshing
        self.store.clear()
        print("Customer care knowledge base refreshed successfully!")
        print("All conversation histories have been cleared.")
    
    def list_knowledge_base_documents(self):
        """List all scraped documentation pages"""
        metadata = self.load_metadata()
        pages = metadata.get("pages", {}) if isinstance(metadata, dict) else {}
        if not pages:
            print("No documentation pages loaded.")
            return

        print(f"\nThredd Cards API Documentation ({len(pages)} pages):")
        print("-" * 60)
        for url, info in pages.items():
            print(f"📄 {info.get('title', url)}")
            print(f"   URL: {url}")
            print(f"   Section: {info.get('section') or '—'}")
            print()
    
    def knowledge_search(self, query, k=6):
        """Perform similarity search for customer care related information"""
        if not hasattr(self, 'vectorstore'):
            return []
        
        docs = self.vectorstore.similarity_search(query, k=k)
        
        print(f"\nFound {len(docs)} relevant sections in knowledge base:")
        print("-" * 50)
        for i, doc in enumerate(docs, 1):
            source = doc.metadata.get('source_file', 'Unknown')
            print(f"{i}. Source: {source}")
            print(f"   Content preview: {doc.page_content[:100]}...")
            print()
        
        return docs

def main():
    try:
        # Initialize the Thredd Cards API docs chatbot
        print("💳 Initializing Thredd Cards API Documentation Assistant...")
        print("This assistant answers questions from the Thredd Cards API docs (https://cardsapidocs.thredd.com).")
        print("The chatbot remembers your conversation context within a session.")

        chatbot = CustomerCareChatbot()

        if hasattr(chatbot, 'conversational_rag_chain'):
            print("\n✅ Thredd Cards API Assistant initialized successfully!")
            print("\n" + "="*70)
            print("💳 THREDD CARDS API DOCUMENTATION ASSISTANT 💳")
            print("="*70)
            print("\nI can help you with:")
            print("🔹 Cards & cardholders (create, retrieve, update, replace, PIN, CVV)")
            print("🔹 3D Secure enrolment & mTLS authentication")
            print("🔹 Card controls, limits and balances")
            print("🔹 Card tokenisation & payment tokens")
            print("🔹 API endpoints, request/response fields and error codes")

            print("\nAvailable commands:")
            print("• Type any Thredd Cards API question")
            print("• 'docs' - View scraped documentation pages")
            print("• 'refresh' - Re-scrape the documentation")
            print("• 'history' - View conversation history")
            print("• 'clear' - Clear conversation memory")
            print("• 'sessions' - List active sessions")
            print("• 'search [query]' - Search the documentation")
            print("• 'help' - Show this menu")
            print("• 'exit' - End conversation")

            # Default session for client interaction
            session_id = "client_session"

            # Thredd Cards API assistant interface
            while True:
                user_input = input(f"\n{'='*20}\nYou: ").strip()

                if user_input.lower() == 'exit':
                    print("Thanks for using the Thredd Cards API Assistant! 💳")
                    break

                elif user_input.lower() == 'help':
                    print("\n💳 THREDD CARDS API ASSISTANT COMMANDS:")
                    print("-" * 40)
                    print("• Ask any Thredd Cards API question")
                    print("• 'docs' - View scraped documentation pages")
                    print("• 'refresh' - Re-scrape the documentation")
                    print("• 'history' - View conversation history")
                    print("• 'clear' - Clear conversation memory")
                    print("• 'sessions' - List active sessions")
                    print("• 'search [your query]' - Search the documentation")
                    print("• 'help' - Show this menu")
                    print("• 'exit' - End conversation")
                    continue
                    
                elif user_input.lower() == 'docs':
                    chatbot.list_knowledge_base_documents()
                    continue
                    
                elif user_input.lower() == 'refresh':
                    chatbot.refresh_knowledge_base()
                    continue
                    
                elif user_input.lower() == 'history':
                    chatbot.get_conversation_history(session_id)
                    continue
                    
                elif user_input.lower() == 'clear':
                    chatbot.clear_memory(session_id)
                    continue
                    
                elif user_input.lower() == 'sessions':
                    chatbot.list_sessions()
                    continue
                    
                elif user_input.lower().startswith('search '):
                    search_query = user_input[7:]  # Remove 'search ' prefix
                    if search_query:
                        chatbot.knowledge_search(search_query)
                    else:
                        print("Please provide a search query. Example: 'search 3d secure'")
                    continue

                elif not user_input:
                    continue

                print("\n💳 Thredd Cards API Assistant: ", end="")
                response = chatbot.query(user_input, session_id)
                print(response)

        else:
            print("❌ Failed to initialize Thredd Cards API Assistant.")
            print("Please check your environment variables and network access to https://cardsapidocs.thredd.com.")

    except Exception as e:
        print(f"❌ Error initializing Thredd Cards API Assistant: {str(e)}")
        print("Please check your environment setup:")
        print("1. Ensure GROQ_API_KEY is set in your .env file")
        print("2. Make sure you have network access to https://cardsapidocs.thredd.com")
        print("3. Verify all required packages are installed (pip install -r requirements.txt)")

if __name__ == "__main__":
    main()