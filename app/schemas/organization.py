# TODO: Escrever docstrings

# DEPENDENCIES IMPORTS
from datetime import datetime
from pydantic import BaseModel
from typing import Optional



# SCHEMAS
class OrganizationBase(BaseModel):
    """
    """
    name : str
    slug: str



class OrganizationResponse(OrganizationBase):
    """
    """
    id: int
    owner_id: int
    created_at: datetime



class OrganizationUpdate(BaseModel):
    """
    """
    name: Optional[str] = None
    slug: Optional[str] = None
    