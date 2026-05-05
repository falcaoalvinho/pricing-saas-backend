"""
TODO:
 - Escrever docstrings de todas as funções
 - Paginação de requests com grandes quantidades de dados
"""

# PROJECT IMPORTS
from app.repositories import product_repository



# FUNCTIONS
def calculate_price(cost, margin):
    """
    """
    return round(cost * (1 + margin / 100), 2)



def create_product(db, product_data, current_user):
    """
    """
    suggested_price = calculate_price(
        product_data.cost,
        product_data.margin_percentage
    )

    return product_repository.create_product(
        db,
        product_data,
        suggested_price,
        current_user
    )



def read_product_list(db, current_user):
    """
    """
    return product_repository.read_product_list(db, current_user)



def read_product(db, product_id, current_user):
    """
    """
    return product_repository.read_product(db, product_id, current_user)



def update_product(db, product_id, new_data, current_user):
    """
    """
    new_suggested_price = calculate_price(new_data.cost, new_data.margin_percentage)

    return product_repository.update_product(
        db,
        product_id,
        new_data,
        new_suggested_price,
        current_user
    )



def delete_product(db, product_id, current_user):
    """
    """
    return product_repository.delete_product(db, product_id, current_user)