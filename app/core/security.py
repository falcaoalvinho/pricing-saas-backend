from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_hash(text: str) -> str:
    return pwd_context.hash(text)

def verify_password(plain_password: str, hashed_passaword: str) -> bool:
    return pwd_context.verify(plain_password, hashed_passaword)