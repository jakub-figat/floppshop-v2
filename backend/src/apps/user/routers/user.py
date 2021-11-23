from uuid import UUID

from fastapi import Depends, Response, status
from fastapi.routing import APIRouter
from fastapi_jwt_auth import AuthJWT

from src.apps.user.models import User
from src.apps.user.schemas import UserInputSchema, UserLoginInputSchema, UserOutputSchema, UserRegisterInputSchema
from src.apps.user.services import UserAuthService
from src.dependencies import authenticate_user
from src.utils.schemas import AccessTokenOutputSchema

router = APIRouter(prefix="/users")


@router.post("/register", tags=["users"], status_code=status.HTTP_201_CREATED, response_model=UserOutputSchema)
async def register_user(user_register_schema: UserRegisterInputSchema) -> UserOutputSchema:
    user_schema = await UserAuthService.register_user(user_register_schema)
    return user_schema


@router.post("/login", tags=["users"], status_code=status.HTTP_200_OK, response_model=AccessTokenOutputSchema)
async def login_user(
    user_login_schema: UserLoginInputSchema, auth_jwt: AuthJWT = Depends()
) -> AccessTokenOutputSchema:
    user = await UserAuthService.authenticate(**user_login_schema.dict())
    access_token = auth_jwt.create_access_token(subject=str(user.id))

    return AccessTokenOutputSchema(access=access_token)


@router.get("/", tags=["users"], status_code=status.HTTP_200_OK, response_model=list[UserOutputSchema])
async def get_users(request_user: User = Depends(authenticate_user)) -> list[UserOutputSchema]:
    return [UserOutputSchema.from_orm(user) for user in await User.all()]


@router.get("/me", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def get_logged_user(request_user: User = Depends(authenticate_user)) -> UserOutputSchema:
    return UserOutputSchema.from_orm(request_user)


@router.get("/{user_id}", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def get_user(user_id: UUID, request_user: User = Depends(authenticate_user)) -> UserOutputSchema:
    return UserOutputSchema.from_orm(await User.get(id=user_id))


@router.put("/{user_id}", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def update_user(
    input_schema: UserInputSchema, request_user: User = Depends(authenticate_user)
) -> UserOutputSchema:
    await User.filter(id=request_user.id).update(**input_schema.dict())
    return UserOutputSchema.from_orm(await User.get(id=request_user.id))


@router.delete("/{user_id}", tags=["users"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(request_user: User = Depends(authenticate_user)):
    await User.filter(id=request_user.id).delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)