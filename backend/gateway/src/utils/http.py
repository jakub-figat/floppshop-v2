from typing import Optional, Union

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from httpx import AsyncClient, Response


class HTTPService:
    def __init__(self, request: Request) -> None:
        self.request = request

    def _get_auth_header(self) -> Optional[dict[str, str]]:
        if (auth_header := self.request.headers.get("authorization")) is not None:
            return {"Authorization": auth_header}

    def _process_json(self, json) -> Optional[Union[list, dict]]:
        if json is not None:
            return jsonable_encoder(json)

    def _raise_from_response(self, response: Response) -> None:
        """
        If response has status code from 4xx or 5xx groups, raise fastapi.HTTPException
        with status code and body of the response. If valid, do nothing.
        :param response:
        :return:
        """
        if response.is_error:
            if response.status_code >= 500:
                raise RuntimeError(response.text)

            raise HTTPException(detail=response.json()["detail"], status_code=response.status_code)

    async def make_request(
        self, *, url: str, method: str = "GET", json=None, raise_exception: bool = False, **kwargs
    ) -> Response:
        json = self._process_json(json)

        async with AsyncClient() as client:
            response = await client.request(url=url, method=method, json=json, **kwargs)

        if raise_exception and response.is_error:
            self._raise_from_response(response)

        return response

    async def make_auth_request(
        self, *, url: str, method: str = "GET", json=None, raise_exception: bool = False, **kwargs
    ) -> Response:
        auth_header = self._get_auth_header()
        return await self.make_request(
            url=url, method=method, json=json, raise_exception=raise_exception, headers=auth_header, **kwargs
        )
