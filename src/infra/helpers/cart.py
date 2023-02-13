""" product helpers """
# pylint: disable=E0401
from decimal import Decimal
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.infra.models.products import Product

freight = Decimal(10.00) # move to env

class CartHelper:
    """ helpers to product """
    def __init__(self, database: Session):
        self.database = database

    
    async def convert(self, items):
        to_list = items.split(',')
        return to_list

    async def subtotal(self, price: Decimal, quantity: int):
        sub = price * quantity
        return sub

    async def total(self, price: Decimal, quantity: int):
        total = (price * quantity) + freight
        return total

    