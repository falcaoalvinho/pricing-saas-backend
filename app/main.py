from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers.product_router import router as product_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_router)

@app.get("/")
def read_root():
    return {"message": "API running"}