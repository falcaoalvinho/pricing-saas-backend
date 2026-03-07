from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    cost: float
    margin_percentage: float