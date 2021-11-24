from typing import Union

from fastapi import status
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient
from starlette.responses import JSONResponse

from src.apps.user.schemas import UserOutputSchema, UserRegisterSchema
from src.settings import api_urls


class UserService:
    @classmethod
    async def handle_register(cls, user_register_schema: UserRegisterSchema) -> Union[UserOutputSchema, JSONResponse]:
        async with AsyncClient() as client:
            request_data = jsonable_encoder(user_register_schema.dict())
            response = await client.post(api_urls.user.register, json=request_data)

        if response.status_code != status.HTTP_201_CREATED:
            return JSONResponse(content=response.json(), status_code=response.status_code)

        return UserOutputSchema(**response.json())
