from pydantic import BaseSettings


class RabbitMQSettings(BaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_PORT: int
