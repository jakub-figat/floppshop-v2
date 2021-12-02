import datetime as dt
from decimal import Decimal
from uuid import uuid4

import pytest

from src.apps.order.models import Category, Order, Product, User
from src.apps.order.schemas import (
    CategoryInputSchema,
    OrderProductAddInputSchema,
    ProductAddInputSchema,
    UserInputSchema,
)
from src.apps.order.services import OrderService
from src.settings import APIUrls


@pytest.fixture
def order_schema() -> OrderProductAddInputSchema:
    categories = [
        CategoryInputSchema(external_id=uuid4(), name="Category_1"),
        CategoryInputSchema(external_id=uuid4(), name="Category_2"),
    ]

    user = UserInputSchema(
        external_id=uuid4(),
        first_name="first_name",
        last_name="second_name",
        email="string@string.io",
        username="username",
        date_of_birth=dt.date(2019, 1, 1),
        is_active=True,
    )

    product = ProductAddInputSchema(
        external_id=uuid4(), name="product_name", price=Decimal("20.88"), count=17, categories=categories
    )

    return OrderProductAddInputSchema(product=product, user=user)


@pytest.mark.asyncio
async def test_order_service_can_create_service(order_schema: OrderProductAddInputSchema, api_urls: APIUrls, use_db):
    await OrderService.add_product_to_order(order_schema=order_schema)

    user = await User.first()
    product = await Product.first().select_related("order")
    order = await Order.first().select_related("user")

    assert order.user == user
    assert product.order == order
    assert product.external_id == order_schema.product.external_id
    assert user.external_id == order_schema.user.external_id
    assert await Category.all().count() == 2
