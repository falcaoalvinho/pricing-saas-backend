from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate, ProductListResponse, ProductResponse, ProductUpdate
from app.db.session import SessionLocal, get_db
from app.services import product_service

router = APIRouter(prefix="/products")

db = get_db()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.get("/", response_model=ProductListResponse)
def get_product_list():
    ...

@router.get("/", response_model=ProductResponse)
def get_product():
    ...

@router.put("/", response_model=ProductResponse)
def update_product():
    ...

@router.delete("/", response_model=ProductResponse)
def delete_product():
    ...
