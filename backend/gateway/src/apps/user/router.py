from fastapi import APIRouter, status

from src.apps.user.schemas import AccessTokenOutputSchema, UserLoginSchema, UserOutputSchema, UserRegisterSchema
from src.apps.user.services import UserService

router = APIRouter(prefix="/users")


@router.post("/register", response_model=UserOutputSchema, status_code=status.HTTP_201_CREATED)
async def register_user(user_register_schema: UserRegisterSchema) -> UserOutputSchema:
    return await UserService.register(user_register_schema)


@router.post("/login", response_model=AccessTokenOutputSchema, status_code=status.HTTP_200_OK)
async def login_user(user_login_schema: UserLoginSchema) -> AccessTokenOutputSchema:
    return await UserService.login(user_login_schema)
