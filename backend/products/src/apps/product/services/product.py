from uuid import UUID

from src.apps.product.models import Category, Product
from src.apps.product.schemas import ProductInputSchema
from src.utils.validators import validate_ids_exist


class ProductService:
    @classmethod
    async def update_product_categories(cls, product: Product, categories: list[UUID]) -> None:
        await validate_ids_exist(ids=categories, model=Category)
        categories = await Category.filter(id__in=categories)
        await product.categories.add(*categories)

    @classmethod
    async def create_product(cls, product_input_schema: ProductInputSchema) -> Product:
        product_data = product_input_schema.dict()
        categories = product_data.pop("categories", None)

        product = await Product.create(**product_data)
        if categories is not None:
            await cls.update_product_categories(product=product, categories=categories)

        return product
