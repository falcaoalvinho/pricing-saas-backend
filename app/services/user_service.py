from app.repositories import user_repository

def create_user(db, user_data):
    return user_repository.create_user(
        db,
        user_data,
    )