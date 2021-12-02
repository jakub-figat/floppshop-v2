import json
from typing import Any

import aio_pika
from aio_pika import DeliveryMode, ExchangeType

from src.settings import settings


class AIOPikaService:
    async def send_message(self, data: dict[str, Any], routing_key: str) -> None:
        connection = await aio_pika.connect(
            host=settings.RABBITMQ_HOST,
            login=settings.RABBITMQ_USERNAME,
            password=settings.RABBITMQ_PASSWORD,
            port=settings.RABBITMQ_PORT,
        )

        async with connection:
            channel = await connection.channel()
            exchange = await channel.declare_exchange(name="user_exchange", type=ExchangeType.TOPIC)
            message = aio_pika.Message(json.dumps(data).encode(), delivery_mode=DeliveryMode.PERSISTENT)

            await exchange.publish(message, routing_key=routing_key)
