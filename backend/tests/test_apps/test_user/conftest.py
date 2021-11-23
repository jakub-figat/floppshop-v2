import datetime as dt

import pytest

from src.apps.user.schemas import UserInputSchema, UserOutputSchema, UserRegisterInputSchema
from src.apps.user.services import UserRegisterService


@pytest.fixture()
def user_register_data() -> dict[str, str]:
    return {
        "first_name": "name",
        "last_name": "name",
        "username": "username",
        "email": "email@email.example",
        "password": "tost123",
        "password_2": "tost123",
        "date_of_birth": "2020-01-01",
    }


@pytest.fixture()
def user_input_schema() -> UserInputSchema:
    return UserInputSchema(
        first_name="name",
        last_name="name",
        username="username_input",
        email="emailinput@email.email",
        date_of_birth=dt.date(2020, 1, 1),
    )


@pytest.fixture()
def user_register_schema() -> UserRegisterInputSchema:
    return UserRegisterInputSchema(
        first_name="name",
        last_name="name",
        username="usernameregister",
        email="emailregister@email.email",
        password="tost123",
        password_2="tost123",
        date_of_birth=dt.date(2020, 1, 1),
    )


@pytest.fixture()
def user_register_schema_2() -> UserRegisterInputSchema:
    return UserRegisterInputSchema(
        first_name="name",
        last_name="name",
        username="usernameregister2",
        email="emailregister2@email.emaila",
        password="tost123",
        password_2="tost123",
        date_of_birth=dt.date(2020, 1, 1),
    )


@pytest.fixture()
async def registered_user_1(user_register_data: dict[str, str], use_db) -> UserOutputSchema:
    user_register_schema = UserRegisterInputSchema(**user_register_data)
    return await UserRegisterService.register_user(user_register_schema=user_register_schema)
