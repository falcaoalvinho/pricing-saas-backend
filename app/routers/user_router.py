from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.db.session import SessionLocal, get_db
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

db = get_db()

@router.post(
    "/",
    summary="Create user",
    description="Cria uma instância da entidade user no banco de dados",
    response_model=list[UserResponse])
def create_product(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get(
    "/",
    summary="Read all users",
    description="Retorna todos os registros ta tabela users",
    response_model=list[UserResponse])
def get_user_list(db: Session = Depends(get_db)):
    return user_service.read_user_list(db) 

@router.get(
    "/?user_id={user_id}",
    summary="Read user",
    description="Recebe o id e retorna os dados do respectivo user",
    response_model=UserResponse
    )
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.read_user(db, user_id)

@router.put(
    "/?user_id={user_id}",
    summary="Update user",
    description="Recebe um novo conjunto de dados e um id, e se eles forem diferentes altera no registro com o respectivo id",
    response_model=UserResponse)
def update_user(user_id: int, new_data: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, new_data)

@router.delete(
    "/?user_id={user_id}",
    summary="Delete user",
    description="Recebe um id, e deleta o registro com o respectivo id",
    response_model=list[UserResponse])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id)