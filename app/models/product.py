from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    margin_percentage = Column(Float, nullable=False)
    suggested_price = Column(Float, nullable=False)

    owner = relationship("User", back_populates="products")