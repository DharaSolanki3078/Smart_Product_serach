from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from models.request_response import QueryRequest, SearchResponse
from llm.llm import get_parsed_product_query, query_chroma_with_filters
import uvicorn
# from vectordb.query_db import search_vector_db
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/smart_search")
def smart_search(request: QueryRequest):
    print(f"User Query: {request.query}")
    llm_output = get_parsed_product_query(request.query)
    top_results = query_chroma_with_filters(llm_output)
    print(f"Top results: {top_results}")
    return {"results": top_results}
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)