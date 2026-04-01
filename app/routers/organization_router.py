"""
TODO:
 - Aplicar conceito DRY para uso dos parâmetros 'db' e 'current_user' 
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services import organization_service
from app.schemas.organization import OrganizationBase, OrganizationResponse, OrganizationUpdate
from app.dependencies.auth import get_current_user
from app.db.session import get_db

from app.models.user import User

router = APIRouter(prefix="/organizations", tags=["Organizations"])

db = get_db()

@router.post(
    "/",
    summary="Create organization",
    description="Cria uma instância da entidade organization no banco de dados",
    response_model=OrganizationResponse
    )
def create_organization(organization_data: OrganizationBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[organization] create request was awsered successfully!"}
    return organization_service.create_organization(db, organization_data, current_user)

@router.get(
    "/",
    summary="Read all organizations",
    description="Retorna todas as organizações que o usuário é dono",
    response_model=list[OrganizationResponse]
    )
def get_organization_list(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[organization] get all id request was awsered successfully!"}
    return organization_service.read_organization_list(db, current_user)
    
@router.get(
    "/{organization_id}",
    summary="Read organization",
    description="Recebe o id e retorna a organização do usuário corespondente",
    response_model=OrganizationResponse
    )
def get_organization(organization_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[organization] get by id request was awsered successfully!"}
    return organization_service.read_organization(db, organization_id, current_user)

@router.put(
    "/{organization_id}",
    summary="Update organization",
    description="Recebe um novo conjunto de dados e um id, e se eles forem diferentes altera no registro com respectivo id",
    response_model=OrganizationResponse
    )
def update_organization(organization_id: int, new_data: OrganizationUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[organization] update request was awsered successfully!"}
    return organization_service.update_organization(db, organization_id, new_data, current_user)

@router.delete(
    "/{organization_id}",
    summary="Delete organization",
    description="Recebe um id e delete o respectivo registo no banco",
    response_model=list[OrganizationResponse]
    )
def delete_organization(organization_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[organization] delete request was awsered successfully!"}
    return organization_service.delete_organization(db, organization_id, current_user)