from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Membership(Base):
    __tablename__ = "memberships"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)

    role = Column(String(100), nullable=False)
    created_at = Column(DateTime, default-datetime.now)

    user = relationship("User", back_populates="memberships")
    organization = relationship("Organization", back_populates="memberships")