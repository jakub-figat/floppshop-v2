from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from src.apps.order.models import Order

Tortoise.init_models(["src.apps.orders.models"], "orders")


OrderOutputSchema = pydantic_model_creator(Order, name="OrderOutputSchema")
OrderListOutputSchema = pydantic_queryset_creator(Order, name="OrderListOutputSchema")
