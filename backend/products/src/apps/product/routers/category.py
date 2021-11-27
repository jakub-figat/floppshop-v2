from fastapi import APIRouter, status

from src.apps.product.models import Category
from src.apps.product.schemas.product import CategoryListOutputSchema

category_router = APIRouter(prefix="/categories")


@category_router.get("/", response_model=CategoryListOutputSchema, status_code=status.HTTP_200_OK)
async def get_categories() -> CategoryListOutputSchema:
    return await Category.all()
