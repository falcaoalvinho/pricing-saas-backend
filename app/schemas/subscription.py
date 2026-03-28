from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SubscriptionBase(BaseModel):
    plan: str
    status: str

class SubscriptionCreate(SubscriptionBase):
    organization_id: int
    expires_at: Optional[str] = None

class SubscriptionResponse(SubscriptionBase):
    id: int
    organization_id: int
    started_at: datetime
    expires_at: datetime

class SubscriptionUpdate(BaseModel):
    plan: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None