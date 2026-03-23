from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    name = Column(String(100), nullable=False)
    cost = Column(Float, nullable=False)
    margin_percentage = Column(Float, nullable=False)
    suggested_price = Column(Float, nullable=False)

    owner = relationship("Organization", back_populates="products")