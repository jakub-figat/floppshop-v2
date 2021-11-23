from fastapi import APIRouter, FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.apps.user.routers import router as user_router
from src.settings import settings

app = FastAPI(
    title="FloppShop V2",
    description="Re-write of e-commerce app",
    version="0.1.0",
    docs_url="/api/v1/swagger",
)

root_router = APIRouter(prefix="/api/v1")

root_router.include_router(user_router)

app.include_router(root_router)


register_tortoise(
    app,
    db_url=settings.postgres_url,
    modules=settings.APP_MODELS,
    add_exception_handlers=True,
)
