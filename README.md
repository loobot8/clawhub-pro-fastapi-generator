# ClawHub Pro - FastAPI Production Generator

> Generate production-ready FastAPI applications in seconds.

## Installation

```bash
# Clone the repo (requires GitHub access - provided after purchase)
git clone https://github.com/loobot8/clawhub-pro-fastapi-generator.git
cd clawhub-pro-fastapi-generator

# Make generator executable
chmod +x generators/fastapi-pro-generator/scripts/generate.py

# Add to PATH (optional)
echo 'export PATH="$PATH:$(pwd)/generators/fastapi-pro-generator/scripts"' >> ~/.zshrc
source ~/.zshrc
```

## Usage

```bash
# Generate a new FastAPI app
python3 generators/fastapi-pro-generator/scripts/generate.py \
  --name my-app \
  --features auth,db,redis \
  --output ~/projects
```

### Available Features

- `auth` - JWT authentication + RBAC
- `db` - Async SQLAlchemy + Alembic migrations
- `redis` - Redis caching layer
- `stripe` - Stripe payment integration
- `websockets` - WebSocket support
- `celery` - Background task queue

### Examples

```bash
# Minimal API
generate.py --name minimal-api --features ""

# SaaS backend with auth + database
generate.py --name saas-backend --features auth,db,stripe

# Full-featured app
generate.py --name my-app --features auth,db,redis,stripe,websockets,celery
```

## What You Get

Every generated app includes:

- ✅ Production-ready FastAPI structure
- ✅ Type-safe with Pydantic v2
- ✅ Feature-based modules
- ✅ Async everywhere (SQLAlchemy, Redis, etc.)
- ✅ Health + readiness probes
- ✅ Multi-stage Docker build
- ✅ GitHub Actions CI/CD
- ✅ Test suite with pytest
- ✅ Linting (ruff) and type checking (mypy)
- ✅ Comprehensive README

## Generated Structure

```
your-app/
├── src/app/
│   ├── main.py              # App factory
│   ├── config.py            # Pydantic Settings
│   ├── features/            # Feature modules
│   │   ├── auth/            # JWT auth (if enabled)
│   │   ├── users/
│   │   └── health/
│   ├── core/
│   │   ├── database.py      # DB engine (if db enabled)
│   │   ├── security.py      # Auth utilities (if auth enabled)
│   │   └── errors.py
│   └── shared/              # Shared utilities
├── tests/                   # Full test suite
├── migrations/              # Alembic (if db enabled)
├── .github/workflows/       # CI/CD
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Support

- Email: hey@clawhubpro.com
- Issues: [GitHub Issues](https://github.com/loobot8/clawhub-pro-fastapi-generator/issues)

## License

This is commercial software. One purchase = one developer license.
Not for redistribution.

---

Built with ❤️ using OpenClaw
