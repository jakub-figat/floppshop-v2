from pydantic import BaseSettings


class RabbitMQSettings(BaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_USERNAME: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_PORT: int
