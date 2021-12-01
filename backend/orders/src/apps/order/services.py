from typing import Any
from uuid import UUID

from src.apps.order.models import Category, Order, Product, User
from src.apps.order.schemas import OrderProductAddInputSchema, UserInputSchema


class OrderService:
    async def _create_categories(self, categories: list[dict[str, Any]]):
        existing_categories_ids = set(await Category.all().values_list("external_id", flat=True))
        categories = [
            Category(**category) for category in categories if category["external_id"] not in existing_categories_ids
        ]

        await Category.bulk_create(categories)

    async def _create_user(self, user_schema: UserInputSchema):
        user_data = user_schema.dict()
        external_id = user_data.pop("external_id")
        user, _ = await User.update_or_create(external_id=external_id, defaults=user_data)

        return user

    async def _set_product_categories(self, product: Product, categories: list[dict[str, Any]]) -> None:
        categories_ids = {category["external_id"] for category in categories}
        categories = await Category.filter(id__in=categories_ids)
        await product.categories.add(*categories)

    async def add_product_to_order(self, product_schema: OrderProductAddInputSchema) -> None:
        product_data = product_schema.product.dict()
        user = product_schema.user
        user, _ = await User.update_or_create(defaults=user.dict())
        order = await Order.create(user=user)

        categories = product_data.pop("categories", None)
        if categories is not None:
            await self._create_categories(categories)

        product = await Product.create(**product_data, order=order)
        await self._set_product_categories(product=product, categories=categories)
