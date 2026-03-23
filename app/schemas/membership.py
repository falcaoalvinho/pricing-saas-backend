from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MembershipBase(BaseModel):
    role: str

class MembershipCreate(MembershipBase):
    user_id: int
    organization_id: int

class MembershipResponse(MembershipBase):
    id: int
    user_id: int
    organization_id: int
    role: str
    created_at: datetime

class MembershipUpdate(BaseModel):
    role: Optional[str] = None

    

