""" cart routes """
# pylint: disable=E0401
from typing import List, Union, Optional
from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from api.schemas.cart import CartSchema, CartUpdate
from src.infra.configs.database import get_database
from src.infra.repositories.cart import CartRepository


cart_routes = APIRouter(
    prefix="/cart",
)


@cart_routes.post("/", status_code=status.HTTP_201_CREATED)
async def add_to_cart(product: CartSchema, database: Session = Depends(get_database)):
    """add to cart"""
    product = await CartRepository(database).add_to_cart(product)
    return product


@cart_routes.get("/items/{items}")
async def get_items(
    items: Optional[str] = None, database: Session = Depends(get_database)
):
    """get items from cart"""
    items = await CartRepository(database).get_items(items)
    return items


@cart_routes.post("/update/{cart_id}")
async def update_by_id(
    cart_id: int, payload: CartUpdate, database: Session = Depends(get_database)
):
    """update product data by name"""
    cart = await CartRepository(database).update_by_id(cart_id, payload)
    return cart
