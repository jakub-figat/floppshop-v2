from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from tortoise.contrib.fastapi import register_tortoise

from src.apps.user.routers import router as user_router
from src.settings import settings

app = FastAPI(
    title="FloppShop V2 - Users",
    description="Re-write of e-commerce app - users service",
    version="0.1.0",
    docs_url="/swagger",
)

# === Routing ===

app.include_router(user_router)


# === Tortoise ===

if settings.APP_MODELS:
    register_tortoise(
        app,
        db_url=settings.postgres_url,
        modules=settings.APP_MODELS,
        add_exception_handlers=True,
    )


# === Exception handlers ===


@app.exception_handler(AuthJWTException)
def auth_jwt_exception_handler(request: Request, exception: AuthJWTException) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": exception.message})
