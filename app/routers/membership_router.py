from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.membership import MembershipCreate, MembershipResponse, MembershipUpdate
from app.db.session import get_db

router = APIRouter(prefix="/memberships", tags=["Memberships"])

db = get_db()

@router.post(
    "/",
    summary="Create membership",
    description="Cria uma nova membership no banco de dados vinculada ao usuário atual e uma organização da qual ele faz parte.",
    # response_model=list[MembershipResponse]
)
def create_membership():
    return {"mensage": "[membership] create request was answered successfully!"}

@router.get(
    "/",
    summary="Read all memberships",
    description="Retorna a lista de memberships do usuário atual.",
    # response_model=list[MembershipResponse]
)
def get_membership_list():
    return {"mensage": "[membership] get all request was answered successfully!"}

@router.get(
    "/{membership_id}",
    summary="Read membership",
    description="Retorna uma membership se ele pertencer ao usuário atual.",
    # response_model=MembershipResponse
)
def get_membership():
    return {"mensage": "[membership] get by id request was answered successfully!"}

@router.put(
    "/{membership_id}",
    summary="Update membership",
    description="Atualiza o registro de uma membership do usuário atual.",
    # response_model=MembershipResponse
)
def update_membership():
    return {"mensage": "[membership] update request was answered successfully!"}

@router.delete(
    "/{membership_id}",
    summary="Delete Membership",
    description="Deleta o registro de uma membership do usuário atual.",
    # response_model=list[MembershipResponse]
)
def delete_membership():
    return {"mensage": "[membership] delete request was answered successfully!"}