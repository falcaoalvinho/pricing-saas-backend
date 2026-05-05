from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.membership import MembershipCreate, MembershipResponse, MembershipPatch
from app.dependencies.auth import get_current_user
from app.db.session import get_db
from app.services import membership_service
from app.models.user import User

router = APIRouter(prefix="/memberships", tags=["Memberships"])

db = get_db()

@router.post(
    "/",
    summary="Create membership",
    description="Cria uma nova membership no banco de dados vinculada ao usuário atual e uma organização da qual ele faz parte.",
    response_model=MembershipResponse
)
def create_membership(membership: MembershipCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[membership] create request was answered successfully!"}
    return membership_service.create_membership(db, membership, current_user)



@router.get(
    "/",
    summary="Read all memberships",
    description="Retorna a lista de memberships do usuário atual.",
    response_model=list[MembershipResponse]
)
def get_membership_list(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[membership] get all request was answered successfully!"}
    return membership_service.read_membership_list(db, current_user)



@router.get(
    "/{organization_id}",
    summary="Read membership",
    description="Retorna uma membership se ele pertencer ao usuário atual.",
    response_model=MembershipResponse
)
def get_membership(organization_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[membership] get by id request was answered successfully!"}
    return membership_service.read_membership(db, organization_id, current_user)



@router.patch(
    "/{organization_id}",
    summary="Update membership",
    description="Atualiza o registro de uma membership do usuário atual.",
    response_model=MembershipResponse
)
def update_membership_role(organization_id: int, new_role: MembershipPatch, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[membership] update request was answered successfully!"}
    return membership_service.update_membership_role(db, organization_id, new_role, current_user)



@router.delete(
    "/{organization_id}",
    summary="Delete Membership",
    description="Deleta o registro de uma membership do usuário atual.",
    response_model=list[MembershipResponse]
)
def delete_membership(organization_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # return {"mensage": "[membership] delete request was answered successfully!"}
    return membership_service.delete_membership(db, organization_id, current_user)
