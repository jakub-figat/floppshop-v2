from fastapi import APIRouter, FastAPI

app = FastAPI(
    title="FloppShop V2 - Gateway",
    description="Re-write of e-commerce app - gateway service",
    version="0.1.0",
    docs_url="/api/swagger",
)

# === Routing ===

root_router = APIRouter(prefix="/api")


app.include_router(root_router)


# === Exception handlers ===
