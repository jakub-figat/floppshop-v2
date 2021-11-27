from uuid import UUID

from fastapi import APIRouter, status

from src.apps.product.models import Product
from src.apps.product.schemas import ProductInputSchema, ProductOutputSchema
from src.apps.product.schemas.product import ProductListOutputSchema
from src.apps.product.services import ProductService

product_router = APIRouter(prefix="/products")


@product_router.get("/", response_model=ProductListOutputSchema, status_code=status.HTTP_200_OK)
async def get_products() -> ProductListOutputSchema:
    return await Product.all().prefetch_related("categories")


@product_router.get("/{product_id}", response_model=ProductOutputSchema, status_code=status.HTTP_200_OK)
async def get_product(product_id: UUID) -> ProductOutputSchema:
    return await Product.get(id=product_id).prefetch_related("categories")


@product_router.post("/", response_model=ProductOutputSchema, status_code=status.HTTP_201_CREATED)
async def create_product(product_input_schema: ProductInputSchema) -> ProductOutputSchema:
    return await ProductService.create_product(product_input_schema)
