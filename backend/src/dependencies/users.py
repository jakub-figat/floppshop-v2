from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from src.apps.user.models import User


async def authenticate_user(auth_jwt: AuthJWT = Depends()) -> User:
    """
    Adding this dependency to view function requires user
    to provide JWT Bearer token
    """
    auth_jwt.jwt_required()
    user_id = auth_jwt.get_jwt_subject()
    return await User.filter(id=user_id).first()
