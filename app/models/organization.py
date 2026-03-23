from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey(user.id), nullable=False)
    created_at = Column(Datetime, default=datetime.now)

    owner = relationship("Owner", back_populates="organizations")
    subscription = relationship("Subscription", back_populates="organization")
    
    memberships = relationship("Members", back_populates="organization")
    products = relationship("Product", back_populates="owner")