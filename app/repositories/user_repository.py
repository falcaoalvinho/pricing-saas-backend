from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import create_hash

def create_user(db: Session, user_data):
    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=create_hash(user_data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# Add pagination later
def read_user_list(db: Session):
    response = db.query(User).all()
    return {"users": response}

def read_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()