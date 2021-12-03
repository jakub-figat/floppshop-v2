import datetime as dt
from uuid import UUID

import pytest

from src.apps.order.models import User
from src.apps.order.schemas import UserInputSchema
from src.apps.order.services import UserService


@pytest.fixture
def db_users(use_db) -> list[User]:
    user_1 = User(
        external_id=UUID("832175e9-8062-4261-9688-9b8ede7e4a1a"),
        email="before1@string.io",
        first_name="before_1",
        last_name="before_1",
        username="before_1",
        date_of_birth=dt.date(2019, 1, 1),
    )
    user_2 = User(
        external_id=UUID("e12a5ef1-9a33-4009-9392-fa020c8641b6"),
        email="before2@string.io",
        first_name="before_2",
        last_name="before_2",
        username="before_2",
        date_of_birth=dt.date(2018, 1, 1),
    )

    return [user_1, user_2]


@pytest.fixture
def user_input_schemas() -> list[UserInputSchema]:
    return [
        UserInputSchema(
            external_id=UUID("832175e9-8062-4261-9688-9b8ede7e4a1a"),
            email="string@string.io",
            first_name="first_name",
            last_name="last_name",
            username="username_1",
            date_of_birth=dt.date(2020, 5, 5),
            is_active=True,
        ),
        UserInputSchema(
            external_id=UUID("e12a5ef1-9a33-4009-9392-fa020c8641b6"),
            email="string2@string.io",
            first_name="first_name",
            last_name="last_name",
            username="username_2",
            date_of_birth=dt.date(2020, 1, 1),
            is_active=True,
        ),
    ]


@pytest.mark.asyncio
async def test_user_service_correctly_updates_users(
    user_input_schemas: list[UserInputSchema], db_users: list[User], use_db
):
    await User.bulk_create(db_users)
    await UserService.update_users(user_input_schemas)

    user_schema_1, user_schema_2 = user_input_schemas
    values = ["external_id", "email", "first_name", "last_name", "username", "date_of_birth", "is_active"]

    user_data_1 = await User.get(external_id=user_schema_1.external_id).values(*values)
    user_data_2 = await User.get(external_id=user_schema_2.external_id).values(*values)

    assert user_data_1 == user_schema_1.dict()
    assert user_data_2 == user_schema_2.dict()
