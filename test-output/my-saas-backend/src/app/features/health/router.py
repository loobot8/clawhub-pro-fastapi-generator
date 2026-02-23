"""Health check router"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health")
async def health():
    """Liveness probe — is the process running?"""
    return {"status": "ok"}


@router.get("/ready")
async def ready():
    """Readiness probe — can we serve traffic?"""
    checks = {}
    
    # Add checks here (database, redis, etc.)
    # For now, just return ok
    checks["app"] = "ok"
    
    all_ok = all(v == "ok" for v in checks.values())
    return JSONResponse(
        status_code=200 if all_ok else 503,
        content={
            "status": "ok" if all_ok else "degraded",
            "checks": checks,
        },
    )
