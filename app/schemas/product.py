from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    cost: float
    margin_percentage: float

class ProductCreate(ProductBase):
    user_id: int

class ProductResponse(ProductBase):
    id: int
    suggested_price: float

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    cost: Optional[float] = None
    margin_percentage: Optional[float] = None
