from abc import ABCMeta

from fastapi import Depends

from src.utils.http import HTTPService


class BaseAPIService(metaclass=ABCMeta):
    def __init__(self, http_service: HTTPService = Depends()) -> None:
        self.http_service = http_service
