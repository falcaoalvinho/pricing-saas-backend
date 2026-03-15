from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.product import Product

def create_product(db: Session, product_data, suggested_price, current_user):
    product = Product(
        user_id=current_user.id,
        name=product_data.name,
        cost=product_data.cost,
        margin_percentage=product_data.margin_percentage,
        suggested_price=suggested_price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return read_product_list(db, current_user)

# TODO: add pagination on return
def read_product_list(db, current_user):
    response = db.query(Product).filter(Product.user_id == current_user.id)
    return response

def read_product(db, product_id, current_user):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product == None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if product.user_id == current_user.id:
        return product
    
    else:
        raise HTTPException(status_code=404, detail="O usuário não é dono do produto")

def update_product(db, product_id, new_data, new_suggested_price, current_user):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if product == None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if product.user_id == current_user.id:
        data = new_data.model_dump(exclude_unset=True)
        data["suggested_price"] = new_suggested_price
        

        for key, value in data.items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)

        return product
    else:
        raise HTTPException(status_code=404, detail="O usuário não é dono do produto")

def delete_product(db, product_id, current_user):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product == None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if product.user_id == current_user.id:
        db.delete(product)
        db.commit()

        return read_product_list(db, current_user)
    
    else:
        raise HTTPException(status_code=404, detail="O usuário não é dono do produto")
