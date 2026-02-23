# My Saas Backend

Production-ready FastAPI application generated with **ClawHub Pro**.

## Features

- ✅ JWT authentication with RBAC
- ✅ Async SQLAlchemy with migrations
- ✅ Redis caching layer
- ✅ Multi-stage Docker build
- ✅ GitHub Actions CI/CD
- ✅ Type-safe with Pydantic v2
- ✅ Health + readiness probes
- ✅ Production-ready structure

## Quick Start

```bash
# Install dependencies
uv sync

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run development server
uv run uvicorn src.app.main:app --reload
```

Visit http://localhost:8000/docs for API documentation.

## Testing

```bash
uv run pytest
uv run ruff check .
uv run mypy src/
```

## Deployment

```bash
docker build -t my-saas-backend .
docker run -p 8000:8000 --env-file .env my-saas-backend
```

---

Generated with ❤️ by [ClawHub Pro](https://clawhubpro.com)
