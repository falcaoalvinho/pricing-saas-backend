from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.db.session import SessionLocal, get_db
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])

db = get_db()

@router.post(
    "/",
    summary="Create prouduct",
    description="Cria uma instância da entidade product no banco de dados, calculando automaticamente o suggested_price",
    response_model=list(ProductResponse))
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.get(
    "/",
    summary="Read all products",
    description="Retorna todos os registros ta tabela products",
    response_model=list[ProductResponse])
def get_product_list(db: Session = Depends(get_db)):
    return product_service.read_product_list(db)

@router.get(
    "/?product_id={product_id}",
    summary="Read product",
    description="Recebe o id e retorna os dados do respectivo product", 
    response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.read_product(db, product_id)
    
@router.put(
    "/?product_id={product_id}",
    summary="Update product",
    description="Recebe um novo conjunto de dados e um id, e se eles forem diferentes altera no registro com o respectivo id",
    response_model=ProductResponse)
def update_product(product_id: int, new_data: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, new_data)

@router.delete(
    "/?product_id={product_id}",
    summary="Delete product",
    description="Recebe um id, e deleta o registro com o respectivo id",
    response_model=ProductListResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)

# sketch of patch requisition route
# @router.put("/{product_id}", response_model=ProductResponse)
# def update_product(product_id: int, new_data: ProductUpdate, db: Session = Depends(get_db)):
#     # return product_service.update_product(db, product_id, new_data)
#         return product_service.update_product(
#         db=db,
#         product_id=product_id,
#         name=new_data.name,
#         cost=new_data.cost,
#         margin_percentage=new_data.margin_percentage,
#         )
    
