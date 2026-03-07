from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.services import product_service
from app.db.session import SessionLocal

router = APIRouter(prefix="/products")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)