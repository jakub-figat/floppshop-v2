from fastapi import APIRouter, Depends, status
from fastapi.requests import Request

from src.apps.user.schemas import AccessTokenOutputSchema, UserLoginSchema, UserOutputSchema, UserRegisterSchema
from src.apps.user.services import UserService
from src.utils.http import AuthHTTPService, HTTPService

router = APIRouter(prefix="/users")


@router.post("/register", response_model=UserOutputSchema, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_register_schema: UserRegisterSchema, http_service: HTTPService = Depends()
) -> UserOutputSchema:
    return await UserService(http_service=http_service).register(user_register_schema)


@router.post("/login", response_model=AccessTokenOutputSchema, status_code=status.HTTP_200_OK)
async def login_user(
    user_login_schema: UserLoginSchema, http_service: HTTPService = Depends()
) -> AccessTokenOutputSchema:
    return await UserService(http_service=http_service).login(user_login_schema)


@router.get("/", response_model=list[UserOutputSchema], status_code=status.HTTP_200_OK)
async def get_users(request: Request) -> list[UserOutputSchema]:
    http_service = AuthHTTPService(request=request)
    return await UserService(http_service=http_service).get_users()
