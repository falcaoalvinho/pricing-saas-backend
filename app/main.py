from fastapi import FastAPI

from app.db.base import Base
from app.models.user import User
from app.models.organization import Organization
from app.models.membership import Membership
from app.models.product import Product
from app.models.subscription import Subscription

from app.db.session import engine
from app.routers.product_router import router as product_router
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router
from app.routers.subscription_router import router as subscription_router
from app.routers.organization_router import router as organization_router
from app.routers.membership_router import router as membership_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pricing API",
    description="API para cálculo e gerenciamento de preços com base em custo e margem.",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(subscription_router)
app.include_router(organization_router)
app.include_router(membership_router)

# @app.get("/", summary="Default", tags=["Default"], description="Serve para saber se a API está rodando")
# def read_root():
#     return {"message": "API running"}