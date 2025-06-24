from pydantic import BaseModel
from typing import List, Optional, Union, Literal

# ChromaDB-supported operators
ChromaOperators = Literal["$eq", "$ne", "$gt", "$gte", "$lt", "$lte"]

# Fields on which filters can be applied (both string and numeric types)
FilterField = Literal["price", "rating_score", "rating_count", "category"]

class FilterCondition(BaseModel):
    field: FilterField
    op: ChromaOperators
    value: Union[int, float, str]

class ProductQueryInterpretation(BaseModel):
    product_name: str
    description: Optional[str] = None
    filters: List[FilterCondition]
