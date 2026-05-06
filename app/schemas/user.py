# TODO: Escrever docstrings

# DEPENDENCIES IMPORTS
from datetime import datetime
from pydantic import BaseModel
from typing import Optional



# SCHEMAS
class UserBase(BaseModel):
    """
    """
    name: str
    email: str



class UserCreate(UserBase):
    """
    """
    password: str



class UserResponse(UserBase):
    """
    """
    id: int
    is_active: bool
    created_at: datetime



class UserUpdate(BaseModel):
    """
    """
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

