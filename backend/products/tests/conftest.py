import asyncio
from asyncio import AbstractEventLoop
from functools import reduce

import pytest
from httpx import AsyncClient
from tortoise.contrib.test import finalizer, initializer

from main import app
from src.settings import APIUrls, settings


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def async_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url=f"{settings.DOMAIN}/api") as async_client:
        yield async_client


@pytest.fixture(scope="function")
def use_db():
    modules_dirs = reduce(lambda list_1, list_2: list_1 + list_2, settings.APP_MODELS.values())
    initializer(modules_dirs)
    yield
    finalizer()


@pytest.fixture(scope="session")
def api_urls() -> APIUrls:
    return APIUrls()
