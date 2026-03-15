from app.repositories.user_repository import read_user_by_email
from app.core.security import verify_password
from app.core.jwt import create_access_token

def authenticate_user(db, email: str, password: str):
    user = read_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user

def login(db, email: str, password: str):
    user = authenticate_user(db, email, password)

    if not user:
        return None

    token = create_access_token(
        {"sub": str(user.id)}
    )

    return token