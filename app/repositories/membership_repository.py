"""
TODO: 
 - Escrever todas as docstrings das funções
 - Adicionar paginação a requests que acessam muitos recursos
"""

# PROJECT IMPORTS
from app.models.membership import Membership



# FUNCTIONS
def create_membership(db, membership, current_user):
    """
    """
    new_membership = Membership(
        user_id = current_user.id,
        organization_id = membership.organization_id
        )

    db.add(new_membership)
    db.commit()

    return new_membership



def read_membership_list(db, current_user):
    """
    """
    memberships = db.query(Membership).filter(Membership.user_id == current_user.id)
    return memberships



def read_membership(db, organization_id, current_user):
    """
    """
    membership = (db
                    .query(Membership)
                    .filter(Membership.organization_id == organization_id)
                    .filter(Membership.user_id == current_user.id)
                    .first()
                )
    
    return membership



def update_membership_role(db, membership, new_role):
    """
    """
    membership.role = new_role.role

    db.commit()
    db.refresh(membership)

    return membership



def delete_membership(db, membership, current_user):
    """
    """
    db.delete(membership)
    db.commit()

    return read_membership_list(db, current_user)