from typing import Any
from uuid import UUID

from fastapi import Depends
from fastapi.encoders import jsonable_encoder

from src.apps.user.exceptions import auth_exception
from src.apps.user.models import User
from src.apps.user.schemas import UserInputSchema, UserOutputSchema, UserRegisterInputSchema
from src.apps.user.utils import password_context
from src.utils.aio_pika import AIOPikaService


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


class UserService:
    def __init__(self, aio_pika_service: AIOPikaService = Depends()) -> None:
        self.aio_pika_service = aio_pika_service

    async def _send_update_user_event(self, user_schema: UserOutputSchema) -> None:
        user_data = user_schema.dict()
        user_data["external_id"] = user_data.pop("id")
        updated_users = [user_data]

        await self.aio_pika_service.send_message(data=jsonable_encoder(updated_users), routing_key="user.update")

    async def update_user(self, user_id: UUID, user_schema: UserInputSchema) -> UserOutputSchema:
        await User.filter(id=user_id).update(**user_schema.dict())
        user_schema = UserOutputSchema.from_orm(await User.get(id=user_id))
        await self._send_update_user_event(user_schema)

        return user_schema
