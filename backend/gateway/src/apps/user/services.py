from src.apps.user.schemas import AccessTokenOutputSchema, UserLoginSchema, UserOutputSchema, UserRegisterSchema
from src.settings import api_urls
from src.utils.http import HTTPService


class UserService:
    @classmethod
    async def register(cls, user_register_schema: UserRegisterSchema) -> UserOutputSchema:
        response = await HTTPService.make_request(
            url=api_urls.user.register, method="POST", json=user_register_schema.dict()
        )

        return UserOutputSchema(**response.json())

    @classmethod
    async def login(cls, user_login_schema: UserLoginSchema) -> AccessTokenOutputSchema:
        response = await HTTPService.make_request(
            url=api_urls.user.login, method="POST", json=user_login_schema.dict()
        )

        return AccessTokenOutputSchema(**response.json())
