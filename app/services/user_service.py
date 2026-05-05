"""
TODO:
 - Escrever docstrings de todas as funções
 - Paginação de requests com grandes quantidades de dados
"""

# PROJECT REPOSITORIES
from app.repositories import user_repository



# FUNCTIONS
def create_user(db, user_data):
    """
    """
    return user_repository.create_user(db, user_data)



def read_user_list(db):
    """
    """
    return user_repository.read_user_list(db)



def read_user(db, user_id):
    """
    """
    return user_repository.read_user(db, user_id)



def update_user(db, user_id, new_data):
    """
    """
    return user_repository.update_user(db, user_id, new_data)



def delete_user(db, user_id):
    """
    """
    return user_repository.delete_user(db, user_id)