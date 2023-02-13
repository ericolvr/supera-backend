""" user repository """
# pylint: disable=E0401
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.cart import CartSchema
from src.infra.models.cart import Cart
from src.infra.models.products import Product
from src.infra.helpers.cart import CartHelper


class CartRepository:
    """ user repository """
    def __init__(self, database: Session):
        self.database = database

    async def add_to_cart(self, product: CartSchema):
        """ add product to cart """

        new = Cart(
            user_id=product.user_id,
            product_id=product.product_id,
            product_name=product.product_name,
            product_price=product.product_price,
            quantity=product.quantity,
            status=product.status,
            
            subtotal=await CartHelper(self.database) \
                .subtotal(product.product_price, product.quantity),
            
            total=await CartHelper(self.database) \
                .total(product.product_price, product.quantity)

        )
        self.database.add(new)
        self.database.commit()
        self.database.refresh(new)

        return new

    async def get_items(self, items: str):
        result = await CartHelper(self.database).convert(items)
        cart_list = self.database.query(Cart).filter(Cart.id.in_(result)).all()
        return cart_list

    async def update_by_id(self, cart_id: int, payload):
        cart = self.database.query(Cart).filter(Cart.id == cart_id).first()     
        cart.quantity = payload.quantity
        
        cart.subtotal = await CartHelper(self.database) \
            .subtotal(cart.product_price, payload.quantity)
        
        cart.total = await CartHelper(self.database) \
            .total(cart.product_price, payload.quantity)

        self.database.commit()
        self.database.refresh(cart)

        return cart

