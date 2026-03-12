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
def get_product_list(db: Session = Depends(get_db)):
    return product_service.read_product_list(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(user_id: int, db: Session = Depends(get_db)):
    return product_service.read_product(db, user_id)
    
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(user_id: int, new_data: UserUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, user_id, new_data)
    
@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)
