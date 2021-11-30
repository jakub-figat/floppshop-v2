import json
from uuid import UUID

from fastapi import Depends
from fastapi.encoders import jsonable_encoder

from src.apps.product.models import Category, Product
from src.apps.product.schemas import ProductAddInputSchema, ProductInputSchema, ProductOutputSchema
from src.utils.aio_pika import AIOPikaService
from src.utils.validators import validate_ids_exist


class ProductService:
    def __init__(self, aio_pika_service: AIOPikaService = Depends()) -> None:
        self.aio_pika_service = aio_pika_service

    async def update_product_categories(self, product: Product, categories: list[UUID]) -> None:
        await validate_ids_exist(ids=categories, model=Category)
        categories = await Category.filter(id__in=categories)
        await product.categories.add(*categories)

    async def create_product(self, product_input_schema: ProductInputSchema) -> Product:
        product_data = product_input_schema.dict()
        categories = product_data.pop("categories", None)

        product = await Product.create(**product_data)
        if categories is not None:
            await self.update_product_categories(product=product, categories=categories)

        return product

    async def add_product_to_order(
        self, product_id: UUID, user_id: str, product_add_input_schema: ProductAddInputSchema
    ) -> None:
        product = await Product.get(id=product_id)
        await product.fetch_related("categories")

        product_data = (await ProductOutputSchema.from_tortoise_orm(product)).dict()
        product_data["count"] = product_add_input_schema.count
        print(repr(user_id))
        message_data = {
            "product": jsonable_encoder(product_data),
            "user_id": user_id,
        }

        await self.aio_pika_service.send_message(data=message_data, routing_key="order.product.add")
