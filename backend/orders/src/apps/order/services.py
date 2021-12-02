from typing import Any, Optional
from uuid import UUID

from tortoise.transactions import atomic

from src.apps.order.models import Category, Order, Product, User
from src.apps.order.schemas import OrderProductAddInputSchema, UserInputSchema


class OrderService:
    @classmethod
    async def update_categories(cls, categories: list[dict[str, Any]]):
        existing_categories_ids = set(await Category.all().values_list("external_id", flat=True))
        categories = [
            Category(**category) for category in categories if category["external_id"] not in existing_categories_ids
        ]

        await Category.bulk_create(categories)

    @classmethod
    async def update_or_create_user(cls, user_schema: UserInputSchema):
        user_data = user_schema.dict()
        external_id = user_data.pop("external_id")
        user, _ = await User.update_or_create(external_id=external_id, defaults=user_data)

        return user

    @classmethod
    async def set_product_categories(cls, product: Product, categories: list[dict[str, Any]]) -> None:
        categories_ids = {category["external_id"] for category in categories}
        categories = await Category.filter(id__in=categories_ids)
        await product.categories.add(*categories)

    @classmethod
    async def add_product_to_order(cls, order_schema: OrderProductAddInputSchema) -> None:
        product_data = order_schema.product.dict()
        user_schema = order_schema.user
        user = await cls.update_or_create_user(user_schema)
        order = await Order.create(user=user)

        categories = product_data.pop("categories", None)
        if categories is not None:
            await cls.update_categories(categories)

        product = await Product.create(**product_data, order=order)
        await cls.set_product_categories(product=product, categories=categories)


class UserService:
    @classmethod
    def _get_existing_user_by_external_id(cls, user_id: UUID, existing_users: list[User]) -> Optional[User]:
        for user in existing_users:
            if user_id == user.external_id:
                return user

    @classmethod
    @atomic()
    async def _update_users(cls, existing_users: list[User], existing_user_schemas: list[UserInputSchema]) -> None:
        for schema in existing_user_schemas:
            existing_user = cls._get_existing_user_by_external_id(schema.external_id, existing_users)
            existing_user.update_from_dict(schema.dict())
            await existing_user.save(
                update_fields=(
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "date_of_birth",
                )
            )

    @classmethod
    async def update_users(cls, user_schemas: list[UserInputSchema]) -> None:
        existing_users = list(await User.all())
        existing_user_ids = [user.external_id for user in existing_users]
        existing_user_schemas = [schema for schema in user_schemas if schema.external_id in existing_user_ids]

        if existing_user_schemas:
            await cls._update_users(existing_users, existing_user_schemas)
