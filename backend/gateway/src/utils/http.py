from typing import Any, Optional, Union

from fastapi import HTTPException
from fastapi.datastructures import Headers
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient, Response


class HTTPService:
    @classmethod
    def _get_auth_header(cls, headers: Optional[Headers]) -> Optional[dict[str, Any]]:
        if headers is not None and (auth_header := headers.get("authorization")) is not None:
            return {"Authorization": auth_header}

    @classmethod
    def _process_json(cls, json) -> Optional[Union[list, dict]]:
        if json is not None:
            return jsonable_encoder(json)

    @classmethod
    async def make_request(cls, *, url: str, method: str = "GET", json=None, **kwargs) -> Response:
        json = cls._process_json(json)
        auth_headers = cls._get_auth_header(kwargs.pop("headers", None))

        async with AsyncClient() as client:
            response = await client.request(url=url, method=method, json=json, headers=auth_headers, **kwargs)

        if response.is_error:
            raise HTTPException(
                detail=response.json()["detail"],
                status_code=response.status_code,
            )

        return response
