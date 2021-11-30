from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.apps.product.schemas import ProductAddInputSchema, ProductOutputSchema
from src.apps.product.services import ProductService
from src.apps.user.services import UserService

product_router = APIRouter(prefix="/products")


@product_router.get("/", response_model=list[ProductOutputSchema], status_code=status.HTTP_200_OK)
async def get_products(
    user_service: UserService = Depends(), product_service: ProductService = Depends()
) -> list[ProductOutputSchema]:
    await user_service.verify_token()
    return await product_service.get_products()


@product_router.post("/{product_id}", status_code=status.HTTP_200_OK)
async def add_product_to_order(
    product_id: UUID,
    product_add_input_schema: ProductAddInputSchema,
    user_service: UserService = Depends(),
    product_service: ProductService = Depends(),
) -> dict[str, str]:
    await user_service.verify_token()
    return await product_service.add_product_to_order(
        product_id=product_id, product_add_input_schema=product_add_input_schema
    )
