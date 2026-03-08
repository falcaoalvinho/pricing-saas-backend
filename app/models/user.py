from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False) 
    is_active = Column(Bolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now)