from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from app.presentation.api import lifespan
from app.presentation.api.middleware import apply_middleware
from app.presentation.api.router import apply_routes
from presentation.api.healthcheck.router import router as healthcheck_router
from settings.config import settings


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="WeatherAPI",
        docs_url="/api/docs/",
        debug=True,
        lifespan=lifespan,
    )

    app = apply_routes(apply_middleware(app))

    return app


if __name__ == "__main__":

    uvicorn.run(
        "main:create_app",
        factory=True,
        host=settings.SERVICE_API_HOST,
        port=settings.SERVICE_API_PORT,
        log_level="debug",
        reload=True,
        workers=1,
    )
