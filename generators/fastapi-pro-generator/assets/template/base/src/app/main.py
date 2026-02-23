"""FastAPI application factory"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.features.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    settings = get_settings()
    print(f"🚀 Starting {settings.app_name} ({settings.environment})")
    
    # Startup logic here
    yield
    
    # Shutdown logic here
    print(f"👋 Shutting down {settings.app_name}")


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        lifespan=lifespan,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
    )
    
    # Middleware (order matters — last added = first executed)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Routers
    app.include_router(health_router, tags=["health"])
    
    # Feature routers (conditional)
    if {{HAS_AUTH}}:
        from app.features.auth import router as auth_router
        app.include_router(auth_router, prefix="/api", tags=["auth"])
    
    return app


# Create app instance
app = create_app()
