from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field, validator
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from src.apps.product.models import Category, Product

Tortoise.init_models(["src.apps.product.models"], "products")

CategoryOutputSchema = pydantic_model_creator(
    Category,
    name="CategoryOutputSchema",
    include=(
        "id",
        "name",
    ),
)

CategoryListOutputSchema = pydantic_queryset_creator(
    Category,
    name="CategoryListOutputSchema",
    include=(
        "id",
        "name",
    ),
)


class ProductInputSchema(BaseModel):
    name: str = Field(..., max_length=100)
    price: Decimal
    categories: list[UUID] = Field(default_factory=list)


class ProductAddInputSchema(BaseModel):
    count: int

    @validator("count")
    def validate_count(cls, count: int) -> int:
        if count <= 0:
            raise ValueError("Invalid count")

        return count


ProductOutputSchema = pydantic_model_creator(Product, name="ProductOutputSchema")

ProductListOutputSchema = pydantic_queryset_creator(Product, name="ProductListOutputSchema")
