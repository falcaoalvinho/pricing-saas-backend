from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), unique=True, nullable=False)

    plan = Column(String, default="basic", nullable=False)
    status = Column(String, default="active", nullable=False)
    started_at = Column(DateTime, default=datetime.now)
    expires_at = Column(DateTime)

    organization = relationship("Organization", back_populates="subscription")