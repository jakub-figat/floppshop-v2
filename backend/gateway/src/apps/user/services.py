from src.apps.user.schemas import AccessTokenOutputSchema, UserLoginSchema, UserOutputSchema, UserRegisterSchema
from src.settings import api_urls
from src.utils.services import BaseAPIService


class UserService(BaseAPIService):
    async def register(self, user_register_schema: UserRegisterSchema) -> UserOutputSchema:
        response = await self.http_service.make_request(
            url=api_urls.user.register, method="POST", json=user_register_schema.dict(), raise_exception=True
        )

        return UserOutputSchema(**response.json())

    async def login(self, user_login_schema: UserLoginSchema) -> AccessTokenOutputSchema:
        response = await self.http_service.make_request(
            url=api_urls.user.login, method="POST", json=user_login_schema.dict(), raise_exception=True
        )

        return AccessTokenOutputSchema(**response.json())

    async def verify_token(self) -> None:
        await self.http_service.make_request(url=api_urls.token.verify, method="POST", raise_exception=True)

    async def get_users(self) -> list[UserOutputSchema]:
        response = await self.http_service.make_request(url=api_urls.user.all, raise_exception=True)

        return [UserOutputSchema(**user_data) for user_data in response.json()]
