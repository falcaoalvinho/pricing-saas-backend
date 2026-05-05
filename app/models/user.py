# TODO: Escrever Docsting da classe.

# DEPENDENCIES IMPORT
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String  
from sqlalchemy.orm import relationship

# PROJECT IMPORTS
from app.db.base import Base



class User(Base):
    """
    """
    __tablename__ = "users"

    # KEYS
    id = Column(Integer, primary_key=True)
    
    # COLUMNS
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    hashed_password = Column(String(100), nullable=False) 
    is_active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now)

    # RELATIONSHIPS
    memberships = relationship("Membership", back_populates="user")
    organizations = relationship("Organization", back_populates="owner")