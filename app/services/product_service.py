from app.repositories import product_repository
from app.schemas.product import ProductUpdate

def calculate_price(cost, margin):
    return round(cost * (1 + margin / 100), 2)


def create_product(db, product_data, current_user):
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
    return product_repository.read_product_list(db, current_user)

def read_product(db, product_id, current_user):
    return product_repository.read_product(db, product_id, current_user)

def update_product(db, product_id, new_data, current_user):
    new_suggested_price = calculate_price(new_data.cost, new_data.margin_percentage)
    return product_repository.update_product(db, product_id, new_data, new_suggested_price, current_user)

def delete_product(db, product_id, current_user):
    return product_repository.delete_product(db, product_id, current_user)

# sketch of patch service layer method
# def update_product(**kwargs):
#     if kwargs["cost"] == None:
#         product_data = product_repository.read_product(kwargs["db"], kwargs["product_id"])
        
#         return update_product(
#             db = kwargs["db"],
#             product_id = kwargs["product_id"],
#             name = kwargs["name"],
#             cost = product_data.cost,
#             margin_percentage = kwargs["margin_percentage"],
#             )

#     elif kwargs["margin_percentage"] == None:
#         product_data = product_repository.read_product(kwargs["db"], kwargs["product_id"])
        
#         return update_product(
#             db = kwargs["db"],
#             product_id = kwargs["product_id"],
#             name = kwargs["name"],
#             cost = kwargs["cost"],
#             margin_percentage = product_data.margin_percentage,
#             )

#     else:
#         suggested_price = calculate_price(kwargs["cost"], kwargs["margin_percentage"])
#         new_data = ProductUpdate(
#             name = kwargs["name"],
#             cost = kwargs["cost"],
#             margin_percentage = kwargs["margin_percentage"],
#             )
            
#         return product_repository.update_product(kwargs["db"], kwargs["product_id"], new_data, suggested_price)
