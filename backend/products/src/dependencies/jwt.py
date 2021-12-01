import json
from typing import Any

from fastapi import Depends
from fastapi_jwt_auth import AuthJWT


def get_user(auth_jwt: AuthJWT = Depends()) -> dict[str, Any]:
    return json.loads(auth_jwt.get_jwt_subject())
