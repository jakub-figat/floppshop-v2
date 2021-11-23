from uuid import UUID

from fastapi import Response, status
from fastapi.routing import APIRouter

from src.apps.user.models import User
from src.apps.user.schemas import UserInputSchema, UserOutputSchema, UserRegisterInputSchema
from src.apps.user.services import UserRegisterService

router = APIRouter(prefix="/users")


@router.post("/register", tags=["users"], status_code=status.HTTP_201_CREATED, response_model=UserOutputSchema)
async def register_user(user_register_schema: UserRegisterInputSchema) -> UserOutputSchema:
    user_schema = await UserRegisterService.register_user(user_register_schema)
    return user_schema


@router.get("/", tags=["users"], status_code=status.HTTP_200_OK, response_model=list[UserOutputSchema])
async def get_users() -> list[UserOutputSchema]:
    return [UserOutputSchema.from_orm(user) for user in await User.all()]


@router.get("/{user_id}", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def get_user(user_id: UUID) -> UserOutputSchema:
    return UserOutputSchema.from_orm(await User.get(id=user_id))


@router.put("/{user_id}", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def update_user(user_id: UUID, input_schema: UserInputSchema) -> UserOutputSchema:
    await User.filter(id=user_id).update(**input_schema.dict())
    return UserOutputSchema.from_orm(await User.get(id=user_id))


@router.delete("/{user_id}", tags=["users"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID):
    await User.filter(id=user_id).delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
