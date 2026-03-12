from fastapi import APIRouter, Depends
from app.db.session import SessionLocal
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserListResponse, UserUpdate
from app.services import user_service

router = APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_product(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=UserListResponse)
def get_user_list(db: Session = Depends(get_db)):
    return user_service.read_user_list(db) 

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.read_user(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, new_data: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, new_data)

@router.delete("/{user_id}", response_model=UserListResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id)