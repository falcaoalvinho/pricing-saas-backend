from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey(user.id) nullable=False)
    created_at = Column(Datetime, default=datetime.now)

    products = relationship("Product", back_populates="owner")

id: int (PK)
name: str
slug: str (unique)
owner_id: int (FK → users.id)
created_at: datetime