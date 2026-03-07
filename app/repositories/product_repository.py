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