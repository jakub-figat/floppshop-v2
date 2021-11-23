import datetime as dt
from uuid import uuid4

import pytest
from freezegun import freeze_time

from src.apps.user.schemas import UserOutputSchema


@pytest.fixture(scope="module")
def user_schema(request):
    return UserOutputSchema(
        id=uuid4(),
        first_name="Cat",
        last_name="Roomba",
        username="rumbicki",
        email="rumbicki@op.pl",
        date_of_birth=request.param,
        is_active=True,
    )


@pytest.mark.parametrize(
    "user_schema, expected_age",
    [
        (dt.date(2019, 1, 1), 3),
        (dt.date(2019, 1, 6), 2),
        (dt.date(2020, 1, 1), 2),
        (dt.date(2021, 1, 1), 1),
    ],
    indirect=["user_schema"],
)
@pytest.mark.asyncio
@freeze_time("2022-01-01")
async def test_user_schema_returns_correct_age(user_schema: UserOutputSchema, expected_age: int):
    assert user_schema.age == expected_age
