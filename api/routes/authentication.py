""" routes to authentication """
# pylint: disable=E0401
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from api.schemas.users import UserAuth, UserAuthenticated
from src.infra.configs.database import get_database
from src.infra.helpers.users import UserHelper
from src.infra.providers.token import TokenProvider
from src.infra.providers.hash import HashProvider

authentication_routes = APIRouter(
    prefix="/authentication",
)


@authentication_routes.post("/token/", status_code=status.HTTP_201_CREATED)
async def generate_token(
    login_data: UserAuth, database: Session = Depends(get_database)
):
    """send / validated user data to generate token"""
    mobile = login_data.mobile
    password = login_data.password

    user = await UserHelper(database).filter_by_mobile(mobile)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong mobile number or password",
        )

    if user.role == "CLIENT":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role - This user Type cant be authenticate",
        )

    valid_password = await HashProvider.verify_hash(password, user.password)
    if not valid_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password"
        )

    jwt_token = await TokenProvider.create_access_token({"sub": user.mobile})

    return UserAuthenticated(
        fullname=user.fullname, mobile=user.mobile, access_token=jwt_token
    )
