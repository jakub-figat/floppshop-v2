from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class CategoryOutputSchema(BaseModel):
    id: UUID
    name: str


class ProductOutputSchema(BaseModel):
    name: str
    price: Decimal
    categories: list[UUID]
