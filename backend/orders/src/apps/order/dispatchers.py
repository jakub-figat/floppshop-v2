import json
from abc import ABCMeta, abstractmethod

from aio_pika import IncomingMessage

from src.apps.order.schemas import OrderProductAddInputSchema, UserInputSchema
from src.apps.order.services import OrderService, UserService


class BaseQueueDispatcher(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    async def dispatch(cls, message: IncomingMessage) -> None:
        raise NotImplementedError("Not implemented")


class ProductQueueDispatcher(BaseQueueDispatcher):
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


class UserQueueDispatcher(BaseQueueDispatcher):
    @classmethod
    async def update_users(cls, message: IncomingMessage) -> None:
        data = json.loads(message.body.decode("utf-8"))
        print(data)
        user_schemas = [UserInputSchema(**user) for user in data]
        await UserService.update_users(user_schemas)

    @classmethod
    async def dispatch(cls, message: IncomingMessage) -> None:
        dispatchers = {
            "user.update": cls.update_users,
        }
        dispatcher = dispatchers[message.routing_key]
        await dispatcher(message=message)
