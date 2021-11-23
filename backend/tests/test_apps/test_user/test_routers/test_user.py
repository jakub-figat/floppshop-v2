import pytest
from fastapi import status
from httpx import AsyncClient

from src.apps.user.models import User
from src.apps.user.schemas import UserOutputSchema
from src.settings import APIUrls


@pytest.mark.asyncio
async def test_get_user(
    registered_user_1: UserOutputSchema,
    async_client: AsyncClient,
    api_urls: APIUrls,
    use_db,
):

    response = await async_client.get(api_urls.users.list)
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
