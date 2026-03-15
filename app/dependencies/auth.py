from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.user_repository import read_user
from app.core.jwt import SECRET_KEY, JWT_ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        user_id = int(payload.get("sub"))

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )

    user = read_user(db, user_id)

    if not user:
        raise HTTPException(status_code=401)

    return user