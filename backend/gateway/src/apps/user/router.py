from fastapi import APIRouter, Depends, status

from src.apps.user.schemas import AccessTokenOutputSchema, UserLoginSchema, UserOutputSchema, UserRegisterSchema
from src.apps.user.services import UserService

router = APIRouter(prefix="/users")


@router.post("/register", response_model=UserOutputSchema, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_register_schema: UserRegisterSchema, user_service: UserService = Depends()
) -> UserOutputSchema:
    return await user_service.register(user_register_schema)


@router.post("/login", response_model=AccessTokenOutputSchema, status_code=status.HTTP_200_OK)
async def login_user(
    user_login_schema: UserLoginSchema, user_service: UserService = Depends()
) -> AccessTokenOutputSchema:
    return await user_service.login(user_login_schema)


@router.get("/", response_model=list[UserOutputSchema], status_code=status.HTTP_200_OK)
async def get_users(user_service: UserService = Depends()) -> list[UserOutputSchema]:
    return await user_service.get_users()
