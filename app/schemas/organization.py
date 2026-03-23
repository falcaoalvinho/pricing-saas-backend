from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrganizationBase(BaseModel):
    name : str
    slug: str

class OrganizationCreate(OrganizationBase):
    owner_id: int

class OrganizationResponse(OrganizationBase):
    id: int
    owner_id: int
    created_at: datetime

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
