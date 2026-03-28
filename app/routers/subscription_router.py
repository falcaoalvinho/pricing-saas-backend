from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.subscription import SubscriptionCreate, SubscriptionResponse, SubscriptionUpdate
from app.db.session import get_db

router = APIRouter(prefix="/subscription", tags=["Subscriptions"])

db = get_db()

@router.get(
    "/",
    summary="Read subscription",
    description="Retorna a subscription vinculada a organization atual.",
    # response_model=SubscriptionResponse
)
def read_subscription():
    return {"mensage": "[subscription] get subscription request was awnswered successfully!"}

@router.put(
    "/",
    summary="Update subscription",
    description="Atualiza a subscription da organization atual.",
    # response_model=SubscriptionResponse
)
def update_subscription():
    return {"mensage": "[subscription] update subscription request was awnswered successfully!"}

@router.delete(
    "/",
    summary="Delete subscription",
    description="Delete a subscription da organization.",
    # response_model=SubscriptionResponse
)
def delete_subscription():
    return {"mensage": "[subscription] delete subscription request was awnswered successfully!"}