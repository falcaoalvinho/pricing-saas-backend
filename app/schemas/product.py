from typing import List, Optional
from pydantic import BaseModel

class ProductCreate(BaseModel):
    user_id: int
    name: str
    cost: float
    margin_percentage: float

class ProductResponse(BaseModel):
    id: int
    name: str
    cost: float
    margin_percentage: float
    suggested_price: float

class ProductListResponse(BaseModel):
    products: List[ProductResponse]

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    cost: Optional[float] = None
    margin_percentage: Optional[float] = None
