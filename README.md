# 🛒 Smart Product Recommendation System

## [Demo link](https://drive.google.com/file/d/16DA5JMfoMGaJRDVsTaX5lFdZAYKC01rz/view?usp=sharing)

This project is an AI-powered product recommendation system that takes natural language queries from users and returns the most relevant products using:

- **FastAPI** backend  
- **LLM** for query interpretation  
- **Chroma Vector DB** for semantic + metadata filtering  
- A simple **HTML/CSS/JS frontend** to interact with the system  


## Chosen AI Feature

### Option A – Smart Product Search

This project implements a Smart Product Search system that allows users to search for products using natural language queries like:

> “Show me women's wear under $10 with good reviews.”

The system intelligently interprets the query, extracts intent and filters, and returns semantically relevant product recommendations using vector similarity and metadata filtering.

---

## Tools & Libraries Used

| Category         | Tool/Library                        |
|------------------|-------------------------------------|
| LLM              | llama3.3-70B from Groq  (via LangChain)                |
| Orchestration    | LangChain                           |
| Backend          | FastAPI                             |
| Vector Database  | ChromaDB                            |
| Embeddings       | Cohere     |
| Frontend         | HTML, CSS, JavaScript               |
| Product Data     | [FakeStoreAPI](https://fakestoreapi.com/) |

---

## Assumptions

- Product data is fetched from a static source (`https://fakestoreapi.com/products`) and embedded once during ingestion.
- Search is performed only on the product data available from [`https://fakestoreapi.com/products`](https://fakestoreapi.com/products).
- User queries are assumed to be in English
  
---

# Example search queries:
1. Show me women's wear under $10 with good reviews
2. Show me men's wear under $75 with good reviews
3. jewelry
4. jewelry rating above 3
5. Men's clothing under 500$
6. Show me men's clothing under 500$ and rating above 3
---

# Project Setup Instructions

## Backend Setup (FastAPI + LangChain + ChromaDB)

```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install Python dependencies
pip install -r requirements.txt

#4. Create vector db
python vectordb/create_db.py

# 5. Start the FastAPI server
python main.py

## 💻 Frontend Setup & Run Instructions
# 1. Navigate to the frontend directory
cd Frontend

#2. run index.html in chrome


