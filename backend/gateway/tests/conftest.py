import asyncio
from asyncio import AbstractEventLoop

import pytest
from httpx import AsyncClient

from main import app
from src.settings import APIUrls, settings


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def async_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url=f"{settings.DOMAIN}/api/v1/") as async_client:
        yield async_client


@pytest.fixture(scope="session")
def api_urls() -> APIUrls:
    return APIUrls()
