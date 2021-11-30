from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from src.apps.product.models import Product
from src.apps.product.schemas import ProductInputSchema, ProductOutputSchema
from src.apps.product.schemas.product import ProductAddInputSchema, ProductListOutputSchema
from src.apps.product.services import ProductService
from src.dependencies import get_user_id

product_router = APIRouter(prefix="/products")


@product_router.get("/", response_model=ProductListOutputSchema, status_code=status.HTTP_200_OK)
async def get_products() -> ProductListOutputSchema:
    return await Product.all().prefetch_related("categories")


@product_router.get("/{product_id}", response_model=ProductOutputSchema, status_code=status.HTTP_200_OK)
async def get_product(product_id: UUID) -> ProductOutputSchema:
    return await Product.get(id=product_id).prefetch_related("categories")


@product_router.post("/", response_model=ProductOutputSchema, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_input_schema: ProductInputSchema, product_service: ProductService = Depends()
) -> ProductOutputSchema:
    return await product_service.create_product(product_input_schema)


@product_router.post("/{product_id}", status_code=status.HTTP_200_OK)
async def add_product_to_order(
    product_id: UUID,
    product_add_input_schema: ProductAddInputSchema,
    user_id: str = Depends(get_user_id),
    product_service: ProductService = Depends(),
) -> dict[str, str]:
    await product_service.add_product_to_order(
        product_id=product_id, user_id=user_id, product_add_input_schema=product_add_input_schema
    )
    return {"detail": "Product added to order successfully"}
