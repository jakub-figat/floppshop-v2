from src.apps.product.schemas import ProductOutputSchema
from src.settings import api_urls
from src.utils.services import BaseAPIService


class ProductService(BaseAPIService):
    async def get_products(self) -> list[ProductOutputSchema]:
        response = await self.http_service.make_request(url=api_urls.product.all, raise_exception=True)
        return [ProductOutputSchema(**product) for product in response.json()]
