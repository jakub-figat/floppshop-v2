from fastapi import APIRouter, status
from fastapi.requests import Request

from src.apps.product.schemas import ProductOutputSchema
from src.apps.product.services import ProductService
from src.apps.user.services import UserService
from src.utils.http import AuthHTTPService

product_router = APIRouter(prefix="/products")


@product_router.get("/", response_model=list[ProductOutputSchema], status_code=status.HTTP_200_OK)
async def get_products(request: Request) -> list[ProductOutputSchema]:
    http_service = AuthHTTPService(request=request)
    user_service = UserService(http_service=http_service)
    await user_service.verify_token()

    return await ProductService(http_service=http_service).get_products()
