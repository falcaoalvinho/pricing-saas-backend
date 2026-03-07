from app.repositories import product_repository

def calculate_price(cost, margin):
    return cost * (1 + margin / 100)


def create_product(db, product_data):
    price = calculate_price(
        product_data.cost,
        product_data.margin_percentage
    )

    return product_repository.create_product(
        db,
        product_data,
        price
    )