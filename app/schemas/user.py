from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    hashed_password: str
