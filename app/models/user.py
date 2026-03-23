from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    hashed_password = Column(String(100), nullable=False) 
    is_active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now)


    memberships = relationship("Membership" back_populates="user")
    organizations = relationship("Organization", back_populates="owner")