from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    cost: float
    margin_percentage: float

class ProductResponse(BaseModel):
    id: int
    name: str
    cost: float
    margin: float
    suggested_price: float

class ProductListResponse(BaseModel):
    products: List[ProductResponse]

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    cost: Optional[float] = None
    margin: Optional[float] = None
