import pytest
from fastapi import status
from fastapi_jwt_auth import AuthJWT
from httpx import AsyncClient

from src.apps.user.models import User
from src.apps.user.schemas import UserOutputSchema, UserRegisterInputSchema
from src.apps.user.services import UserAuthService
from src.settings import APIUrls


@pytest.fixture()
def user_register_data() -> dict[str, str]:
    return {
        "first_name": "name",
        "last_name": "name",
        "username": "username",
        "email": "email@email.example",
        "password": "tostek123",
        "password_2": "tostek123",
        "date_of_birth": "2020-01-01",
    }


@pytest.fixture()
async def registered_user_1(user_register_data: dict[str, str], use_db) -> UserOutputSchema:
    user_register_schema = UserRegisterInputSchema(**user_register_data)
    return await UserAuthService.register_user(user_register_schema=user_register_schema)


@pytest.fixture()
async def registered_user_1_bearer_token_header(registered_user_1: UserOutputSchema) -> dict[str, str]:
    access_token = AuthJWT().create_access_token(subject=registered_user_1.json())
    return {"Authorization": f"Bearer {access_token}"}


@pytest.mark.asyncio
async def test_get_users(
    registered_user_1: UserOutputSchema,
    registered_user_1_bearer_token_header: dict[str, str],
    async_client: AsyncClient,
    api_urls: APIUrls,
    use_db,
):
    response = await async_client.get(api_urls.users.list, headers=registered_user_1_bearer_token_header)
    assert response.status_code == status.HTTP_200_OK

    response_body = response.json()
    assert len(response_body) == 1
    assert response_body[0]["id"] == str(registered_user_1.id)


@pytest.mark.asyncio
async def test_user_can_register(
    user_register_data: dict[str, str],
    async_client: AsyncClient,
    api_urls: APIUrls,
    use_db,
):
    response = await async_client.post(api_urls.users.register, json=user_register_data)
    assert response.status_code == status.HTTP_201_CREATED

    user = await User.first()

    assert user.username == user_register_data["username"]
