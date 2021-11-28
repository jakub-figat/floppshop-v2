from fastapi import APIRouter, Depends, Response, status

from src.apps.user.models import User
from src.dependencies import authenticate_user

jwt_router = APIRouter(prefix="/token")


@jwt_router.post("/verify", status_code=status.HTTP_204_NO_CONTENT)
async def verify_token(request_user: User = Depends(authenticate_user)) -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)
