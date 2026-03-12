from app.repositories import product_repository

def calculate_price(cost, margin):
    return cost * (1 + margin / 100)


def create_product(db, product_data):
    suggested_price = calculate_price(
        product_data.cost,
        product_data.margin_percentage
    )

    return product_repository.create_product(
        db,
        product_data,
        suggested_price
    )

def read_product_list(db):
    return product_repository.read_product_list(db)

def read_product(db, product_id):
    return product_repository.read_product(db, product_id)

def update_product(db, new_data, product_id):
        new_suggested_price = calculate_price(
        product_data.cost,
        product_data.margin_percentage
    )
    return product_repository.update_product(db, new_data, product_id, new_suggested_price)

def delete_product(db, product_id):
    return product_repository.delete_product(db, new_data)
