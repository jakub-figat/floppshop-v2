from abc import ABCMeta

from src.utils.http import HTTPService


class BaseAPIService(metaclass=ABCMeta):
    def __init__(self, http_service: HTTPService) -> None:
        self.http_service = http_service
