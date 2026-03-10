from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime

class UserListResponse(BaseModel):
    users: List[UserResponse]
