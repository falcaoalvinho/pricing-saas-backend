from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrganizationBase(BaseModel):
    name : str
    slug: str

class OrganizationResponse(OrganizationBase):
    id: int
    owner_id: int
    created_at: datetime

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None

# class OrganizationCreate(OrganizationBase):
    