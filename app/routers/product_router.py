# TODO: Escrever docstrings

#DEPENDENCIES IMPORTS
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# PROJECT IMPORTS
from app.dependencies.auth import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.services import product_service
from app.schemas.product import ProductBase, ProductResponse, ProductUpdate


router = APIRouter(prefix="/products", tags=["Products"])
db = get_db()



# ENDPOINTS FUNCTIONS
@router.post(
    "/",
    summary="Create prouduct",
    description="Cria uma instância da entidade product no banco de dados, calculando automaticamente o suggested_price",
    response_model=list[ProductResponse])
def create_product(
        product: ProductBase,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
    ):
    """
    """
    return product_service.create_product(db, product, current_user)



@router.get(
    "/",
    summary="Read all products",
    description="Retorna todos os registros ta tabela products",
    response_model=list[ProductResponse])
def get_product_list(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    """
    return product_service.read_product_list(db, current_user)



@router.get(
    "/{product_id}",
    summary="Read product",
    description="Recebe o id e retorna os dados do respectivo product", 
    response_model=ProductResponse)
def get_product(
        product_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
    ):
    """
    """
    return product_service.read_product(db, product_id, current_user)



@router.put(
    "/{product_id}",
    summary="Update product",
    description="Recebe um novo conjunto de dados e um id, e se eles forem diferentes altera no registro com o respectivo id",
    response_model=ProductResponse)
def update_product(
        product_id: int,
        new_data: ProductUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
    ):
    """
    """
    return product_service.update_product(db, product_id, new_data, current_user)



@router.delete(
    "/{product_id}",
    summary="Delete product",
    description="Recebe um id, e deleta o registro com o respectivo id",
    response_model=list[ProductResponse])
def delete_product(
        product_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
    ):
    """
    """
    return product_service.delete_product(db, product_id, current_user)