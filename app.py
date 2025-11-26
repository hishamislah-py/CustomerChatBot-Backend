import os
import glob
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
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
        self.metadata_file = "document_metadata.json"
        
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
        
        # FAISS vector store path
        self.faiss_index_path = "faiss_index"
    
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
    
    def process_documents(self, force_rebuild=False):
        """Load and process all supported documents from the data folder"""
        # Get all supported files
        files = self.get_supported_files()
        
        if not files:
            print("No customer care knowledge base documents found in the data folder.")
            print("Please add PDF (.pdf) or Word (.docx, .doc) files to the 'data' folder.")
            return
        
        # Check for changes
        changes_detected, new_metadata = self.check_for_changes(files)
        
        # Check if FAISS index already exists and no changes detected
        if (os.path.exists(self.faiss_index_path) and 
            not force_rebuild and 
            not changes_detected):
            print("Loading existing FAISS index (no changes detected)...")
            self.vectorstore = FAISS.load_local(
                self.faiss_index_path, 
                self.embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            print("Creating new FAISS index from customer care knowledge base...")
            
            # Load all documents
            all_documents = []
            for file_path in files:
                documents = self.load_document(file_path)
                all_documents.extend(documents)
            
            if not all_documents:
                print("No documents were successfully loaded.")
                return
            
            # Split documents into chunks optimized for customer care content
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=800,  # Increased for better context
                chunk_overlap=100,
                separators=["\n\n", "\n", "•", ".", "?", "!", ";", ",", " "]
            )
            self.docs = text_splitter.split_documents(all_documents)
            
            print(f"Split customer care documents into {len(self.docs)} chunks")
            
            # Create FAISS vector store
            self.vectorstore = FAISS.from_documents(
                self.docs,
                self.embeddings
            )
            
            # Save the FAISS index locally
            self.vectorstore.save_local(self.faiss_index_path)
            
            # Save metadata
            self.save_metadata(new_metadata)
            
            print(f"FAISS index saved to {self.faiss_index_path}")
            print(f"Processed {len(files)} customer care documents with {len(self.docs)} total chunks")
    
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

        # Contextualize question prompt for customer care
        contextualize_q_system_prompt = """Given a chat history and the latest user question
        about customer service, support, or related topics, formulate a standalone question
        which can be understood without the chat history.

        IMPORTANT: For simple greetings like "Hi", "Hello", "Good morning", "Thank you", etc.,
        return them exactly as they are without any modification or context from chat history.

        For complex customer care questions, reformulate them if needed to be standalone.
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

        # Customer Care specific QA system prompt
        qa_system_prompt = """You are a knowledgeable Customer Care Assistant representing our company.
        You have access to comprehensive company information including our services, processes, policies, and procedures.
        Use the provided context and conversation history to answer questions about:

        📞 Our Services: Customer support, inquiries, complaints, feedback
        🔍 Product Information: Features, usage, troubleshooting
        📋 Procedures: Step-by-step guides for common issues and requests
        📞 Support: Contact information, operating hours, response times
        💼 Company Operations: Staff roles, escalation procedures, support systems
        provide a concise and accurate answer in 50 to 100 words

        Response Guidelines:

        1. **For Greetings & Pleasantries** ("Hi", "Hello", "Good morning", "Thank you"):
           - Treat each greeting as a fresh interaction
           - Respond warmly and professionally: "Hello! Welcome to our Customer Care services. I'm here to help you with all your concerns. How can I assist you today?"
           - Do NOT reference previous conversations or say "again" or "still here"
           - Keep it simple and welcoming

        2. **For Customer Care Questions**:
           - Provide detailed, helpful responses
           - Use **bold headings** for different sections
           - Structure responses with numbered points or bullet points when appropriate
           - Include specific processes, timelines, and requirements when relevant
           - Reference company policies and procedures from the knowledge base

        3. **For Service-Specific Inquiries**:
           - Explain our services and support options
           - Provide step-by-step processes
           - Mention required information and typical response times
           - Include contact information for next steps

        4. **Professional Tone**:
           - Be helpful, informative, and reassuring
           - Show expertise in customer service matters
           - Acknowledge when information might need verification with a specialist
           - Use appropriate terminology while keeping explanations clear

        5. **If Information Not Available**:
           - Respond: "I don't have that specific information in our current knowledge base. Please contact our support team at +1 (555) 123-4567 or support@example.com for personalized assistance."

        6. **For Complex Questions Only**:
           - Reference previous parts of our conversation when it adds value to complex inquiries
           - For simple greetings, do NOT reference conversation history
           - Avoid mechanical responses like "As per your request" or "Since you asked"
           - Respond naturally as a knowledgeable customer care professional would

        Context from our company knowledge base: {context}"""

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])

        # Create the question-answer chain
        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)

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
        """Query the Customer Care chatbot with memory"""
        if not hasattr(self, 'conversational_rag_chain'):
            return "Sorry, the customer care assistant is not properly initialized. Please check if knowledge base documents are available."
        
        try:
            response = self.conversational_rag_chain.invoke(
                {"input": question},
                config={"configurable": {"session_id": session_id}}
            )
            return response["answer"]
        except Exception as e:
            return f"I apologize, but I encountered an error while processing your request: {str(e)}. Please try again or contact our support team at +1 (555) 123-4567."
    
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
        """List all loaded knowledge base documents"""
        metadata = self.load_metadata()
        if not metadata:
            print("No knowledge base documents loaded.")
            return
        
        print("\nCustomer Care Knowledge Base Documents:")
        print("-" * 60)
        for filename, info in metadata.items():
            print(f"📄 {filename}")
            print(f"   Path: {info['path']}")
            print(f"   Last Modified: {info['last_modified']}")
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
        # Initialize the customer care chatbot
        print("📞 Initializing Customer Care Chatbot...")
        print("This intelligent assistant will help with all customer inquiries using our comprehensive knowledge base.")
        print("The chatbot remembers our conversation context for personalized assistance.")

        chatbot = CustomerCareChatbot()

        if hasattr(chatbot, 'conversational_rag_chain'):
            print("\n✅ Customer Care Chatbot initialized successfully!")
            print("\n" + "="*70)
            print("📞 WELCOME TO YOUR CUSTOMER CARE ASSISTANT 📞")
            print("="*70)
            print("\nI can help you with:")
            print("🔹 Customer support and inquiries")
            print("🔹 Product information and troubleshooting")
            print("🔹 Documentation and procedures")
            print("🔹 Service information and policies")
            print("🔹 Contact details and support information")
            
            print("\nAvailable commands:")
            print("• Type any customer care question")
            print("• 'docs' - View knowledge base documents")
            print("• 'refresh' - Reload knowledge base")
            print("• 'history' - View conversation history")
            print("• 'clear' - Clear conversation memory")
            print("• 'sessions' - List active sessions")
            print("• 'search [query]' - Search knowledge base")
            print("• 'help' - Show this menu")
            print("• 'exit' - End conversation")
            
            # Default session for client interaction
            session_id = "client_session"
            
            # Customer Care chatbot interface
            while True:
                user_input = input(f"\n{'='*20}\nYou: ").strip()

                if user_input.lower() == 'exit':
                    print("Thank you for using our Customer Care Assistant! Have a great day! 📞")
                    break

                elif user_input.lower() == 'help':
                    print("\n📞 CUSTOMER CARE ASSISTANT COMMANDS:")
                    print("-" * 40)
                    print("• Ask any customer care question")
                    print("• 'docs' - View knowledge base documents")
                    print("• 'refresh' - Reload knowledge base")
                    print("• 'history' - View conversation history")
                    print("• 'clear' - Clear conversation memory")
                    print("• 'sessions' - List active sessions")
                    print("• 'search [your query]' - Search knowledge base")
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
                        print("Please provide a search query. Example: 'search billing issue'")
                    continue
                    
                elif not user_input:
                    continue
                
                print("\n📞 Customer Care Assistant: ", end="")
                response = chatbot.query(user_input, session_id)
                print(response)
                
        else:
            print("❌ Failed to initialize Customer Care Chatbot.")
            print("Please check your environment variables and ensure the 'data' folder contains the customer care knowledge base documents.")

    except Exception as e:
        print(f"❌ Error initializing Customer Care Chatbot: {str(e)}")
        print("Please check your environment setup:")
        print("1. Ensure GROQ_API_KEY is set in your .env file")
        print("2. Make sure the 'data' folder contains your customer care knowledge base PDF")
        print("3. Verify all required packages are installed")

if __name__ == "__main__":
    main()