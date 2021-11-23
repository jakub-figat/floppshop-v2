from typing import Any

from src.apps.user.exceptions import auth_exception
from src.apps.user.models import User
from src.apps.user.schemas import UserOutputSchema, UserRegisterInputSchema
from src.apps.user.utils import password_context


class UserAuthService:
    @classmethod
    async def _hash_password(cls, user_data: dict[str, Any]) -> None:
        password_2 = user_data.pop("password_2")
        user_data["password"] = password_context.hash(password_2)

    @classmethod
    async def register_user(cls, user_register_schema: UserRegisterInputSchema) -> UserOutputSchema:
        user_data = user_register_schema.dict()
        await cls._hash_password(user_data=user_data)

        return UserOutputSchema.from_orm(await User.create(**user_data))

    @classmethod
    async def authenticate(cls, email: str, password: str) -> User:
        user = await User.filter(email=email).first()
        if user is None or not password_context.verify(password, user.password):
            raise auth_exception

        return user
