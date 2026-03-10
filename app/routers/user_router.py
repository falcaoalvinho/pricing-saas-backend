from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserListResponse
from app.services import user_service
from app.db.session import SessionLocal

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