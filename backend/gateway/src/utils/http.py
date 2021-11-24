from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient, Response


class HTTPService:
    @classmethod
    async def make_request(cls, *, url: str, method: str = "GET", json=None, **kwargs) -> Response:
        if json is not None:
            json = jsonable_encoder(json)

        async with AsyncClient() as client:
            response = await client.request(url=url, method=method, json=json, **kwargs)

        if response.is_error:
            raise HTTPException(
                detail=response.json()["detail"],
                status_code=response.status_code,
            )

        return response
