"""
TODO: 
 - Escrever docstrings
 - Definir parâmetros para as funções dos endpoints
 - Criar chamadas da layer de serviços
 - Corigir "reponse_model"s comentados
 - Recuperar imports comentados
"""

# DEPENDENCIES IMPORTS
from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# PROJECT DEPENDENCIES
from app.db.session import get_db
# from app.schemas.subscription import SubscriptionCreate, SubscriptionResponse, SubscriptionUpdate


router = APIRouter(prefix="/subscription", tags=["Subscriptions"])
db = get_db()



# ENDPOINTS FUNCTIONS
@router.get(
    "/",
    summary="Read subscription",
    description="Retorna a subscription vinculada a organization atual.",
    # response_model=SubscriptionResponse
)
def read_subscription():
    """
    """
    return {"mensage": "[subscription] get subscription request was awnswered successfully!"}



@router.put(
    "/",
    summary="Update subscription",
    description="Atualiza a subscription da organization atual.",
    # response_model=SubscriptionResponse
)
def update_subscription():
    """
    """
    return {"mensage": "[subscription] update subscription request was awnswered successfully!"}



@router.delete(
    "/",
    summary="Delete subscription",
    description="Delete a subscription da organization.",
    # response_model=SubscriptionResponse
)
def delete_subscription():
    """
    """
    return {"mensage": "[subscription] delete subscription request was awnswered successfully!"}