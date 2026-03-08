from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services import user_service
from app.db.session import SessionLocal

router = APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users")
def create_product(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)