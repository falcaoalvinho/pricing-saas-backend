#TODO: Escrever docstrings

# DEPENDENCIES IMPORTS
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# PROJECT IMPORTS
from app.db.session import get_db
from app.schemas.auth import Token
from app.services.auth_service import login


router = APIRouter(prefix="/auth", tags=["Auth"])



# FUNCTIONS
@router.post("/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    """
    token = login(
        db,
        form_data.username,
        form_data.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }