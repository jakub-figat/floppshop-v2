from asyncio import AbstractEventLoop
from functools import partial
from typing import Type

import aio_pika
from aio_pika import ExchangeType, IncomingMessage

from src.apps.order.dispatchers import BaseQueueDispatcher, ProductQueueDispatcher, UserQueueDispatcher
from src.settings import settings


async def on_message(message: IncomingMessage, dispatcher_class: Type[BaseQueueDispatcher]) -> None:
    await dispatcher_class.dispatch(message=message)
    await message.ack()


async def listen(loop: AbstractEventLoop) -> None:
    connection = await aio_pika.connect_robust(
        host=settings.RABBITMQ_HOST,
        login=settings.RABBITMQ_DEFAULT_USER,
        password=settings.RABBITMQ_DEFAULT_PASS,
        port=settings.RABBITMQ_PORT,
        loop=loop,
    )

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    product_exchange = await channel.declare_exchange(name="product_exchange", type=ExchangeType.TOPIC)
    product_queue = await channel.declare_queue(name="product_queue", durable=True)
    await product_queue.bind(exchange=product_exchange, routing_key="order.product.*")
    await product_queue.consume(partial(on_message, dispatcher_class=ProductQueueDispatcher))

    user_exchange = await channel.declare_exchange(name="user_exchange", type=ExchangeType.TOPIC)
    user_queue = await channel.declare_queue(name="user_queue", durable=True)
    await user_queue.bind(exchange=user_exchange, routing_key="user.*")
    await user_queue.consume(partial(on_message, dispatcher_class=UserQueueDispatcher))
