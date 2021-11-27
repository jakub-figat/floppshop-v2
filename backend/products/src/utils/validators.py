from typing import Type
from uuid import UUID

from fastapi import HTTPException, status
from tortoise import Model


async def validate_ids_exist(ids: list[UUID], model: Type[Model]) -> None:
    ids_set = set(ids)
    if len(ids_set) != await model.filter(id__in=ids_set).count():
        raise HTTPException(
            detail=f"{model.__name__} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
