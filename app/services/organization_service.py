from app.repositories import organization_repository
from fastapi import HTTPException

def create_organization(db, organization_data, current_user):
    return organization_repository.create_organization(db, organization_data, current_user)

def read_organization_list(db, current_user):
    return organization_repository.read_organization_list(db, current_user)

def read_organization(db, organization_id, current_user):
    return organization_repository.read_organization(db, organization_id, current_user)

def update_organization(db, organization_id, new_data, current_user):
    if organization_id == current_user.id:
        return organization_repository.update_organization(db, organization_id, new_data, current_user)

    else:
        raise HTTPException(status_code=404, detail="A organização não pertence ao usuário!")

def delete_organization(db, organization_id, current_user):
    if organization_id == current_user.id:
        return organization_repository.delete_organization(db, organization_id, current_user)
    
    else:
        raise HTTPException(status_code=404, detail="A organização não pertecence ao usuário")
