from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal, get_db
from app.schemas.product import ProductCreate
from app.services import product_service

router = APIRouter(prefix="/products")

db = get_db()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)
