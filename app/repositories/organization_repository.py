from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.organization import Organization

def create_organization(db: Session, organization_data, current_user):
    organization = Organization(
        owner_id = current_user.id,
        name = organization_data.name,
        slug = organization_data.slug
    )

    db.add(organization)
    db.commit()

    return organization

def read_organization_list(db, current_user):
    organizations = db.query(Organization).filter(Organization.owner_id == current_user.id)
    return organizations

def read_organization(db, organization_id, current_user):
    organization = db.query(Organization).filter(Organization.owner_id == current_user.id).filter(Organization.owner_id == organization_id).first()

    if organization == None:
        raise HTTPException(status_code=404, detail="Organização não encontrada")

    return organization

def update_organization(db, organization_id, new_data, current_user):
    organization = read_organization(db, organization_id, current_user)

    data = new_data.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(organization, key, value)

    db.commit()
    db.refresh(organization)

    return organization

def delete_organization(db, organization_id, current_user):
    organization = read_organization(db, organization_id, current_user)

    db.delete(organization)
    db.commit()

    return read_organization_list(db, current_user)