import asyncio

from fastapi import FastAPI, status
from tortoise.contrib.fastapi import register_tortoise

from src.settings import settings
from src.utils.aio_pika import listen

app = FastAPI(
    title="FloppShop V2 - Products",
    description="Re-write of e-commerce app - products service",
    version="0.1.0",
    docs_url="/api/swagger",
)


@app.get("/health", status_code=status.HTTP_200_OK)
async def make_health_check() -> dict[str, str]:
    return {"detail": "Healthy"}


# === Routing ===


# === Tortoise ===

if settings.APP_MODELS:
    register_tortoise(
        app,
        db_url=settings.postgres_url,
        modules=settings.APP_MODELS,
        add_exception_handlers=True,
    )


# === Exception handlers ===


# === Lifecycle hooks ===


@app.on_event("startup")
def startup() -> None:
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(listen(loop=loop))
