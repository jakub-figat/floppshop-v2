from fastapi import Depends
from fastapi_jwt_auth import AuthJWT


def get_user_id(auth_jwt: AuthJWT = Depends()) -> str:
    return auth_jwt.get_jwt_subject()
