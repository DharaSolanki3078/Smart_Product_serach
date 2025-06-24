import requests
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from config import chroma_db
from langchain_core.documents import Document
from uuid import uuid4

def create_db(api_url, persist_directory="./chroma_db"):
    # API call
    response = requests.get(api_url)
    products = response.json()

    # Example: assuming data is a list of dicts with 'content' and 'meta'
    documents = []
    for product in products:
        # Create content from title and description
        content = f"{product.get('title', '')}: {product.get('description', '')}"
        
        # Extract relevant metadata
        metadata = {
            "product_id": product.get('id'),
            "category": product.get('category'),
            "price": product.get('price'),
            "rating_score": product.get('rating', {}).get('rate'),
            "rating_count": product.get('rating', {}).get('count'),
            "image_url": product.get('image')
        }
        
        doc = Document(page_content=content, metadata=metadata)
        documents.append(doc)


    # Create Chroma DB and add documents
    uuids = [str(uuid4()) for _ in range(len(documents))]

    chroma_db.add_documents(documents=documents, ids=uuids)
    return chroma_db

if __name__ == "__main__":
    api_url = "https://fakestoreapi.com/products/"  # Replace with your actual API URL
    db = create_db(api_url)
