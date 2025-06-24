# llm/groq_llm.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import json
from langchain.schema import HumanMessage
from parsers.product_parser import ProductQueryInterpretation, FilterCondition
from langchain_core.prompts import load_prompt
from config import chroma_db, chat_groq
from typing import List, Dict, Any
from pydantic import ValidationError
def get_parsed_product_query(user_query: str) -> ProductQueryInterpretation:
    prompt_template = load_prompt("prompts/prompt.yaml")
    formatted_prompt = prompt_template.format(query=user_query)

    messages = [HumanMessage(content=formatted_prompt)]
    
    response = chat_groq(messages).content.strip()
    print(f"LLM response: {response}")
    # Extract substring from first '{' to last '}'
    start = response.find('{')
    end = response.rfind('}')
    if start != -1 and end != -1 and end > start:
        response = response[start:end+1]
    else:
        raise ValueError(f"Could not find valid JSON object in LLM response:\n{response}")

    try:
        json_output = json.loads(response)
        parsed = ProductQueryInterpretation(**json_output)
        return parsed
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM did not return valid JSON: {e}\n\nLLM output:\n{response}")
    except ValidationError as e:
        raise ValueError(f"LLM output does not match expected structure: {e}\n\nRaw output:\n{response}")
    



def build_chroma_where(filters: List[FilterCondition]) -> Dict[str, Any]:
    """
    Builds a ChromaDB compatible where clause from filter conditions.
    
    ChromaDB expects filters in the format:
    {
        "$and": [
            {"field1": {"$operator1": value1}},
            {"field2": {"$operator2": value2}}
        ]
    }
    """
    if not filters:
        return {}
        
    where_conditions = []
    for f in filters:
        # Create individual condition in format {"field": {"$op": value}}
        condition = {f.field: {f.op: f.value}}
        where_conditions.append(condition)
    
    # If only one condition, return it directly
    if len(where_conditions) == 1:
        return where_conditions[0]
    
    # Otherwise, combine with $and operator
    return {"$and": where_conditions}


def query_chroma_with_filters(
    query_obj: ProductQueryInterpretation,
    top_k: int = 3
):
    where = build_chroma_where(query_obj.filters)
    print(f"Filter conditions: {where}")
    if query_obj.product_name == None:
        query_obj.product_name = ""
    query_text = f"{query_obj.product_name or ''} {query_obj.description or ''}".strip()
    print(f"Query text: {query_text}")
    if where == {} or len(where)==0:
         results = chroma_db.similarity_search_with_relevance_scores(
        query=query_text,
        k=top_k,
    ) 
    else:
    # Perform search
        results = chroma_db.similarity_search_with_relevance_scores(
            query=query_text,
            k=top_k,
            filter=where
        )
    print(f"Raw results: {results}")

    return [
        {
            "content": doc.page_content,
            "metadata": doc.metadata,
            "score": score
        }
        for doc, score in results
    ]
