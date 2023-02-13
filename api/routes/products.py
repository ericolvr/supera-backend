""" product routes """
# pylint: disable=E0401
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.schemas.products import ProductSchema, ProductUpdate
from api.routes.authentication_util import logged_user
from src.infra.configs.database import get_database
from src.infra.repositories.products import ProductRepository


product_routes = APIRouter(prefix="/products")


@product_routes.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductSchema, database: Session = Depends(get_database)
):
    """create new product"""
    new = await ProductRepository(database).create_product(product)
    return new


@product_routes.get("/")
async def list_all(
    offset: int = 0, limit: int = 100, database: Session = Depends(get_database)
):
    """list all products - paginated"""
    product_list = await ProductRepository(database).list_all(offset, limit)
    return product_list


@product_routes.get("/filter/{param}")
async def filter_by(param: str, database: Session = Depends(get_database)):
    """order products by param"""
    product_list = await ProductRepository(database).filter_by(param)
    return product_list


@product_routes.patch("/update/{name}")
async def update_by_name(
    name: str,
    new_data: ProductUpdate,
    token=Depends(logged_user),
    database: Session = Depends(get_database),
):
    """update product data by name"""
    product = await ProductRepository(database).update_by_name(name, new_data)
    return product


@product_routes.delete("/delete/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_name(
    name: str, token=Depends(logged_user), database: Session = Depends(get_database)
):
    """delete product by name"""
    return await ProductRepository(database).delete_by_name(name)


@product_routes.get("/order/{param}")
async def by_param(param: str, database: Session = Depends(get_database)):
    product_list = await ProductRepository(database).by_param(param)
    return product_list

    