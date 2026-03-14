from sqlalchemy.orm import Session

from app.models.product import Product

def create_product(db: Session, product_data, suggested_price):
    product = Product(
        user_id=product_data.user_id,
        name=product_data.name,
        cost=product_data.cost,
        margin_percentage=product_data.margin_percentage,
        suggested_price=suggested_price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return read_product_list(db)

# TODO: add pagination on return
def read_product_list(db):
    response = db.query(Product).all()
    return {"products": response}

def read_product(db, product_id):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db, product_id, new_data, new_suggested_price):
    data = new_data.model_dump(exclude_unset=True)
    data["suggested_price"] = new_suggested_price
    
    product = db.query(Product).filter(Product.id == product_id).first()

    for key, value in data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product

# TODO: add error handling
def delete_product(db, product_id):
    product = db.query(Product).filter(Product.id == product_id).first()

    db.delete(product)
    db.commit()

    return read_product_list(db)