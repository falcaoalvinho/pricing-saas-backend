"""
TODO:
Decidir se devo continuar com o router de organization

Na teoria poderia acessar as informações para cada um dos usuários
pela tabela membership, a questão é.

Será que fazer um único router que lida com as dua tabelas é uma boa prática?

Provavelmente não, porque atrapalha manutenabilidade e abre espaço para erros feios,
por ser mais dificil gerencias o conjunto de operações nas tabelas via um padrão de 
URL só.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.organization import OrganizationCreate, OrganizationResponse, OrganizationUpdate
from app.db.session import get_db

router = APIRouter(prefix="/organizations", tags=["Organizations"])

db = get_db()

@router.post(
    "/",
    summary="Create organization",
    description="Cria uma instância da entidade organization no banco de dados",
    # response_model=OrganizationResponse
    )
def create_organization(organization: OrganizationCreate, db: Session = Depends(get_db)):
    return {"mensage": "[organization] create request was awsered successfully!"}

@router.get(
    "/",
    summary="Read all organizations",
    description="Retorna todas as organizações que o usuário é dono",
    # response_model=list[OrganizationResponse]
    )
def get_organization_list(db: Session = Depends(get_db)):
    return {"mensage": "[organization] get all id request was awsered successfully!"}
    
@router.get(
    "/{organization_id}",
    summary="Read organization",
    description="Recebe o id e retorna a organização do usuário corespondente",
    # response_model=OrganizationResponse
    )
def get_organization(db: Session = Depends(get_db)):
    return {"mensage": "[organization] get by id request was awsered successfully!"}

@router.put(
    "/{organization_id}",
    summary="Update organization",
    description="Recebe um novo conjunto de dados e um id, e se eles forem diferentes altera no registro com respectivo id",
    # response_model=OrganizationResponse
    )
def update_organization():
    return {"mensage": "[organization] update request was awsered successfully!"}

@router.delete(
    "/{organization_id}",
    summary="Delete organization",
    description="Recebe um id e delete o respectivo registo no banco",
    # response_model=list[OrganizationResponse]
    )
def delete_organization():
    return {"mensage": "[organization] delete request was awsered successfully!"}