""" product helpers """
# pylint: disable=E0401
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.infra.models.products import Product


class ProductHelper:
    """ helpers to product """
    def __init__(self, database: Session):
        self.database = database

    async def get_by_name(self, name: str):
        """ check product already exists """
        product = self.database.query(Product).filter(Product.name == name).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"product: {name} not found",
            )

        return product
