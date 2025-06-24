# 🛒 Smart Product Recommendation System

This project is an AI-powered product recommendation system that takes natural language queries from users and returns the most relevant products using:

- 🌐 **FastAPI** backend  
- 🧠 **LangChain + Groq LLM** for query interpretation  
- 🔎 **Chroma Vector DB** for semantic + metadata filtering  
- 💻 A simple **HTML/CSS/JS frontend** to interact with the system  

---

# ⚙️ Project Setup Instructions

## 🔧 Backend Setup (FastAPI + LangChain + ChromaDB)

```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Start the FastAPI server
python main.py

## 💻 Frontend Setup & Run Instructions

```bash
# 1. Navigate to the frontend directory
cd Frontend

#2. run index.html in chrome
