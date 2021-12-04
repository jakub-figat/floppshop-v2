from decimal import Decimal
from uuid import UUID

from humps import camelize
from pydantic import BaseModel


class CategoryOutputSchema(BaseModel):
    id: UUID
    name: str

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class ProductOutputSchema(BaseModel):
    id: UUID
    name: str
    price: Decimal
    categories: list[CategoryOutputSchema]

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class ProductAddInputSchema(BaseModel):
    count: int

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
