"""utils to autehntication """
# pylint: disable=E0401
import logging

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from src.infra.configs.database import get_database
from src.infra.providers.token import TokenProvider
from src.infra.helpers.users import UserHelper

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


async def logged_user(
    token: str = Depends(oauth2_schema), database: Session = Depends(get_database)
):
    """authentication"""

    try:
        mobile = await TokenProvider.verify_access_token(token)
    except JWTError:
        logging.error("Error generating token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )

    if not mobile:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )

    user = await UserHelper(database).filter_by_mobile(mobile)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )

    return user
