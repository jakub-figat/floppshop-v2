from uuid import UUID

from src.apps.product.schemas import ProductAddInputSchema, ProductOutputSchema
from src.settings import api_urls
from src.utils.services import BaseAPIService


class ProductService(BaseAPIService):
    async def get_products(self) -> list[ProductOutputSchema]:
        response = await self.http_service.make_request(url=api_urls.product.all, raise_exception=True)
        return [ProductOutputSchema(**product) for product in response.json()]

    async def add_product_to_order(
        self, product_id: UUID, product_add_input_schema: ProductAddInputSchema
    ) -> dict[str, str]:
        response = await self.http_service.make_auth_request(
            url=api_urls.product.detail.format(product_id),
            method="POST",
            json=product_add_input_schema.dict(),
            raise_exception=True,
        )
        return response.json()
