from fastapi import APIRouter, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.apps.product.router import product_router
from src.apps.user.router import router as user_router

app = FastAPI(
    title="FloppShop V2 - Gateway",
    description="Re-write of e-commerce app - gateway service",
    version="0.1.0",
    docs_url="/api/swagger",
)


# === Middleware ===

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_headers="*",
    allow_methods="*",
)


@app.get("/health", status_code=status.HTTP_200_OK)
async def make_health_check() -> dict[str, str]:
    return {"detail": "Healthy"}


# === Routing ===

root_router = APIRouter(prefix="/api")

root_router.include_router(user_router)
root_router.include_router(product_router)


app.include_router(root_router)


# === Exception handlers ===
