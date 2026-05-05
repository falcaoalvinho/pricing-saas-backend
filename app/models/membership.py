# TODO: Escrever Docsting da classe.

# DEPENDENCIES IMPORTS
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# PROJECT IMPORTS
from app.db.base import Base



class Membership(Base):
    """
    """
    __tablename__ = "memberships"

    # KEYS
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)

    # COLUMNS
    role = Column(String(100), default="guest") 
    created_at = Column(DateTime, default=datetime.now)

    # RELATIONSHIPS
    user = relationship("User", back_populates="memberships")
    organization = relationship("Organization", back_populates="memberships")