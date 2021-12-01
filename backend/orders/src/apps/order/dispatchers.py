import json

from aio_pika import IncomingMessage

from src.apps.order.schemas import OrderProductAddInputSchema
from src.apps.order.services import OrderService


class ProductQueueDispatcher:
    @classmethod
    async def add_product_to_order(cls, message: IncomingMessage) -> None:
        data = json.loads(message.body.decode("utf-8"))
        await OrderService().add_product_to_order(product_schema=OrderProductAddInputSchema(**data))

    @classmethod
    async def dispatch(cls, message: IncomingMessage) -> None:
        dispatchers = {
            "order.product.add": cls.add_product_to_order,
        }
        dispatcher = dispatchers[message.routing_key]
        await dispatcher(message=message)
