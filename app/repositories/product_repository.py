from sqlalchemy.orm import Session
from app.models.product import Product

def create_product(db: Session, product_data, suggested_price):
    product = Product(
        name=product_data.name,
        cost=product_data.cost,
        margin_percentage=product_data.margin_percentage,
        suggested_price=suggested_price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def read_product_list(db):
    ...

def read_product(db, product_id):
    ...

def update_product(db, product_id, new_data, new_suggested_price):
    ...

def delete_product(db, product_id):
    ...