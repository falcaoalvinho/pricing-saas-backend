"""
TODO:
    - Garantia de que a aplicação não vai criar vínculos iguais (mesmo id para user e organization)
"""
from app.repositories import membership_repository
from app.repositories import organization_repository
from fastapi import HTTPException



def create_membership(db, membership, current_user):
    organization = organization_repository.read_organization(db, membership.organization_id, current_user)

    if organization == None:
        raise HTTPException(status_code=404, detail="A organização não foi encontrada ou o usuário atual não é o proprietário")

    else: 
        return membership_repository.create_membership(db, membership, current_user)



def read_membership_list(db, current_user):
    return membership_repository.read_membership_list(db, current_user)



def read_membership(db, organization_id, current_user):
    membership = membership_repository.read_membership(db, organization_id, current_user)

    if membership == None:
        raise HTTPException(status_code=404, detail="Vínculo não encontrado ou inexistente")

    else:
        return membership



def update_membership_role(db, organization_id, new_role, current_user):
    membership = membership_repository.read_membership(db, organization_id, current_user)
    
    if membership == None:
        raise HTTPException(status_code=404, detail="Vínculo não encontrado ou inexistente")

    # if membership.owner_id != current_user.id:
    #     raise HTTPException(status_code=404, detail="O usuário atual não é proprietário da organização, e não pode alterar o registro")

    return membership_repository.update_membership_role(db, membership, new_role)
    


def delete_membership(db, organization_id, current_user):
    membership =  membership_repository.read_membership(db, organization_id, current_user)

    if membership == None:
        raise HTTPException(status_code=404, detail="Vínculo não encontrado ou inexistente")

    return membership_repository.delete_membership(db, membership, current_user)
    