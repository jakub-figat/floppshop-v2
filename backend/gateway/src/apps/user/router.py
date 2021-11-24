from fastapi import APIRouter, status

from src.apps.user.schemas import UserOutputSchema, UserRegisterSchema
from src.apps.user.services import UserService

router = APIRouter(prefix="/users")


@router.post("/register", response_model=UserOutputSchema, status_code=status.HTTP_201_CREATED)
async def register_user(user_register_schema: UserRegisterSchema) -> UserOutputSchema:
    return await UserService.handle_register(user_register_schema)
