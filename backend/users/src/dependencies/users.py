from typing import Optional

from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from src.apps.user.exceptions import invalid_jwt_user_exception
from src.apps.user.models import User


async def authenticate_user(auth_jwt: AuthJWT = Depends()) -> User:
    """
    Adding this dependency to view function requires user
    to provide JWT Bearer token
    """
    auth_jwt.jwt_required()
    user_id = auth_jwt.get_jwt_subject()
    user = await User.filter(id=user_id).first()

    if user is None:
        raise invalid_jwt_user_exception

    return user
