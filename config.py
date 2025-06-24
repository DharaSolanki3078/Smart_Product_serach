from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
import os
from langchain_cohere import CohereEmbeddings

cohere_embeddings = CohereEmbeddings(
    cohere_api_key=os.getenv("COHERE_API_KEY"),  
    model="embed-english-v3.0"  
)
# Chroma DB connection setup
CHROMA_DB_PATH = "/home/bacancy/Desktop/Product_rec/chroma_db"
chroma_db = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=cohere_embeddings
)

# LangChain ChatGroq setup
chat_groq = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)