from typing import Any

from src.apps.user.models import User
from src.apps.user.schemas import UserOutputSchema, UserRegisterInputSchema
from src.apps.user.utils import password_context


class UserRegisterService:
    @classmethod
    async def _hash_password(cls, user_data: dict[str, Any]) -> None:
        password_2 = user_data.pop("password_2")
        user_data["password"] = password_context.hash(password_2)

    @classmethod
    async def register_user(cls, user_register_schema: UserRegisterInputSchema) -> UserOutputSchema:
        user_data = user_register_schema.dict()
        await cls._hash_password(user_data=user_data)

        return UserOutputSchema.from_orm(await User.create(**user_data))
