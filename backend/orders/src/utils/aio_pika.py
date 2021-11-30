from asyncio import AbstractEventLoop

import aio_pika
from aio_pika import ExchangeType, IncomingMessage

from src.apps.order.dispatchers import ProductQueueDispatcher
from src.settings import settings


async def on_message(message: IncomingMessage) -> None:
    await ProductQueueDispatcher.dispatch(message=message)
    await message.ack()


async def listen(loop: AbstractEventLoop) -> None:
    connection = await aio_pika.connect_robust(
        host=settings.RABBITMQ_HOST,
        login=settings.RABBITMQ_USERNAME,
        password=settings.RABBITMQ_PASSWORD,
        port=settings.RABBITMQ_PORT,
        loop=loop,
    )

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    product_exchange = await channel.declare_exchange(name="product_exchange", type=ExchangeType.TOPIC)
    product_queue = await channel.declare_queue(name="product_queue", durable=True)

    await product_queue.bind(exchange=product_exchange, routing_key="order.product.*")
    await product_queue.consume(on_message)
