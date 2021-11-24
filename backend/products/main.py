from fastapi import APIRouter, FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.settings import settings

app = FastAPI(
    title="FloppShop V2 - Products",
    description="Re-write of e-commerce app - products service",
    version="0.1.0",
    docs_url="/api/swagger",
)

# === Routing ===

root_router = APIRouter(prefix="/api")


app.include_router(root_router)


# === Tortoise ===

if settings.APP_MODELS:
    register_tortoise(
        app,
        db_url=settings.postgres_url,
        modules=settings.APP_MODELS,
        add_exception_handlers=True,
    )


# === Exception handlers ===
