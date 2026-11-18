from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import dashboard, health, water

app = FastAPI(
    title="JalDrishti AI API",
    description=(
        "Environmental water intelligence API. Demo records are synthetic; "
        "predictions are not official measurements or drinking-water certifications."
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origin.strip()
        for origin in __import__("os")..getenv(
            "CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
        ).split(",")
        if origin.strip()
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(water.router, prefix="/api/v1")


@app.get("/")
def root() -> dict[str, str]:
    return {"project": "JalDrishti AI", "docs": "/docs", "health": "/api/v1/health"}
