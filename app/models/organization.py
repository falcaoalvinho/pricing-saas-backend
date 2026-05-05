# TODO: Escrever Docsting da classe.

# DEPENDENCIES IMPORTS
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# PROJECT IMPORTS
from app.db.base import Base



#MODEL
class Organization(Base):
    """
    """
    __tablename__ = "organizations"

    # KEYS
    id = Column(Integer, primary_key=True)

    # COLUMNS
    name = Column(String(100), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # RELATIONSHIPS
    owner = relationship("User", back_populates="organizations")
    subscription = relationship("Subscription", back_populates="organization")
    
    memberships = relationship("Membership", back_populates="organization") 
    products = relationship("Product", back_populates="owner")