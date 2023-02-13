""" user routes """
# pylint: disable=E0401
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.schemas.users import UserInput
from api.routes.authentication_util import logged_user
from src.infra.configs.database import get_database
from src.infra.repositories.users import UserRepository


user_routes = APIRouter(
    prefix='/users',
)


@user_routes.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserInput, #request: Request,
    database: Session = Depends(get_database)):
    """ create new user """
    new = await UserRepository(database).create_user(user)#, request)
    return new


@user_routes.get('/')
async def list_all(offset: int = 0, limit: int = 100, token=Depends(logged_user),
    database: Session = Depends(get_database)):
    """list all users """
    users_list = await UserRepository(database).list_all(offset, limit)
    return users_list


@user_routes.get('/{role}')
async def list_by_role(role: str, offset: int = 0, limit: int = 100, 
    token=Depends(logged_user), database: Session = Depends(get_database)):
    """list user by role - can be paginated """
    users_list = await UserRepository(database).list_by_role(role, offset, limit)
    return users_list

    """
        Como os usuários nao foram colocados no contexto, fiz parcial.
        Afim de separar os usuarios entre client e admin
    """

