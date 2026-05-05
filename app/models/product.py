# TODO: Escrever Docsting da classe.

# DEPENDENCIES IMPORTS
from sqlalchemy import Column, Float, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

# PROJECT IMPORTS
from app.db.base import Base



# MODEL
class Product(Base):
    """
    """
    __tablename__ = "products"

    # KEYS
    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    
    # COLUMNS
    name = Column(String(100), nullable=False)
    cost = Column(Float, nullable=False)
    margin_percentage = Column(Float, nullable=False)
    suggested_price = Column(Float, nullable=False)

    # RELATIONSHIPS
    owner = relationship("Organization", back_populates="products")