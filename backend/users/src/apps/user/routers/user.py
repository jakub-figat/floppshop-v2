from uuid import UUID

from fastapi import Depends, Response, status
from fastapi.routing import APIRouter
from fastapi_jwt_auth import AuthJWT

from src.apps.user.models import User
from src.apps.user.schemas import UserInputSchema, UserLoginInputSchema, UserOutputSchema, UserRegisterInputSchema
from src.apps.user.services import UserAuthService, UserService
from src.dependencies import authenticate_user
from src.utils.schemas import AccessTokenOutputSchema

user_router = APIRouter(prefix="/users")


@user_router.post("/register", tags=["users"], status_code=status.HTTP_201_CREATED, response_model=UserOutputSchema)
async def register_user(
    user_register_schema: UserRegisterInputSchema, user_auth_service: UserAuthService = Depends()
) -> UserOutputSchema:
    user_schema = await user_auth_service.register_user(user_register_schema)
    return user_schema


@user_router.post("/login", tags=["users"], status_code=status.HTTP_200_OK, response_model=AccessTokenOutputSchema)
async def login_user(
    user_login_schema: UserLoginInputSchema, auth_jwt: AuthJWT = Depends()
) -> AccessTokenOutputSchema:
    user = await UserAuthService.authenticate(**user_login_schema.dict())
    user_schema = UserOutputSchema.from_orm(user)
    access_token = auth_jwt.create_access_token(subject=user_schema.json())

    return AccessTokenOutputSchema(access=access_token)


@user_router.get(
    "/",
    tags=["users"],
    dependencies=[Depends(authenticate_user)],
    status_code=status.HTTP_200_OK,
    response_model=list[UserOutputSchema],
)
async def get_users() -> list[UserOutputSchema]:
    return [UserOutputSchema.from_orm(user) for user in await User.all()]


@user_router.get("/me", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def get_logged_user(request_user: User = Depends(authenticate_user)) -> UserOutputSchema:
    return UserOutputSchema.from_orm(request_user)


@user_router.get(
    "/{user_id}",
    tags=["users"],
    dependencies=[Depends(authenticate_user)],
    status_code=status.HTTP_200_OK,
    response_model=UserOutputSchema,
)
async def get_user(user_id: UUID) -> UserOutputSchema:
    return UserOutputSchema.from_orm(await User.get(id=user_id))


@user_router.put("/me", tags=["users"], status_code=status.HTTP_200_OK, response_model=UserOutputSchema)
async def update_user(
    input_schema: UserInputSchema,
    request_user: User = Depends(authenticate_user),
    user_service: UserService = Depends(),
) -> UserOutputSchema:
    return await user_service.update_user(user_id=request_user.id, user_schema=input_schema)
