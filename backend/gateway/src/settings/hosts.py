from pydantic import BaseSettings


class ServiceSettings(BaseSettings):
    USERS_ADDRESS: str
    PRODUCTS_ADDRESS: str
    ORDERS_ADDRESS: str
