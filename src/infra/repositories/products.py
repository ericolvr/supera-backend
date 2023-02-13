"""product repository """
# pylint: disable=E0401
from typing import Any, List
from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from api.schemas.products import ProductSchema
from src.infra.models.products import Product
from src.infra.helpers.products import ProductHelper


class ProductRepository:
    """product repository class """
    def __init__(self, database: Session):
        self.database = database
    
    async def create_product(self, product: ProductSchema) -> Product:
        """create product """
        await ProductRepository(self.database).check_exists(product.name)

        new = Product(
            name=product.name,
            price=product.price,
            score=product.score,
            image=product.image
        )

        self.database.add(new)
        self.database.commit()
        self.database.refresh(new)

        return new

    async def check_exists(self, name: str) -> Any:
        """ check product already exists before insert """
        product = self.database.query(Product) \
            .filter(Product.name == name).first()

        if product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product: {product} has already exists!")

        return

    async def list_all(self, offset: int, limit: int) -> List[Product]:
        """ list all products with pagination """
        products = self.database.query(Product) \
            .offset(offset).limit(limit).all()
        return products

    async def filter_by(self, param: str) -> Any:
        """filter to product - order """
        products = self.database.query(Product).filter(Product.param == param).all()
        return products

    async def update_by_name(self, name: str, new_data):
        """ update user by name """
        result = await ProductHelper(self.database).get_by_name(name)

        if not result:
            return result

        data = new_data.dict(exclude_unset=True)
        for key, value in data.items():
            setattr(result, key, value)
        self.database.add(result)
        self.database.commit()
        self.database.refresh(result)

        return result


    async def delete_by_name(self, name: str):
        """ delete user by name"""
        result = await ProductHelper(self.database).get_by_name(name)
        if not result:
            return result

        self.database.delete(result)
        self.database.commit()
        return {"message": "Product deleted from database",
            "status_code": status.HTTP_204_NO_CONTENT} 

    async def by_param(self, param):
        if param == 'name':
            products = self.database.query(Product).order_by(asc(Product.name)).all()
            return products
        
        elif param == 'score':
            products = self.database.query(Product).order_by(desc(Product.score)).all()
            return products
        
        elif param == 'price':
            roducts = self.database.query(Product).order_by(asc(Product.price)).all()
            return products
        
        # TODO 
        # after query all records, just filter 
        # predicado - esta feio d+