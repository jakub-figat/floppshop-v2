import datetime as dt
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from src.apps.order.models import Order, User

UserOutputSchema = pydantic_model_creator(User, name="UserOutputSchema")


Tortoise.init_models(["src.apps.order.models"], "orders")


OrderOutputSchema = pydantic_model_creator(Order, name="OrderOutputSchema")
OrderListOutputSchema = pydantic_queryset_creator(Order, name="OrderListOutputSchema")


class UserInputSchema(BaseModel):
    external_id: UUID
    email: str = Field(..., max_length=100)
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    username: str = Field(..., max_length=50)
    date_of_birth: dt.date
    is_active: bool = True


class CategoryInputSchema(BaseModel):
    external_id: UUID
    name: str


class ProductAddInputSchema(BaseModel):
    external_id: UUID
    name: str
    price: Decimal
    count: int
    categories: list[CategoryInputSchema]


class OrderProductAddInputSchema(BaseModel):
    product: ProductAddInputSchema
    user: UserInputSchema
