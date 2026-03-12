from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    cost: float
    margin_percentage: float

class ProductResponse(BaseModel):
    id: int
    name: str
    name: str
    cost: float
    margin: float
    suggested_price: float
