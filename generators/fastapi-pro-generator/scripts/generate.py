#!/usr/bin/env python3
"""
FastAPI Production Generator
Generates production-ready FastAPI applications with best practices baked in.
"""

import argparse
import os
import shutil
from pathlib import Path
from typing import List

TEMPLATE_DIR = Path(__file__).parent.parent / "assets" / "template"

FEATURES = {
    "auth": "JWT authentication with RBAC",
    "db": "Async SQLAlchemy with migrations",
    "stripe": "Stripe payment integration",
    "websockets": "WebSocket support",
    "redis": "Redis caching layer",
    "celery": "Background task queue",
}


def snake_to_title(snake_str: str) -> str:
    """Convert snake_case to Title Case"""
    return " ".join(word.capitalize() for word in snake_str.split("_"))


def generate_app(name: str, features: List[str], output_dir: Path) -> None:
    """Generate FastAPI application"""
    
    print(f"🚀 Generating FastAPI app: {name}")
    print(f"📦 Features: {', '.join(features)}")
    print(f"📁 Output: {output_dir}")
    
    # Create output directory
    app_dir = output_dir / name
    if app_dir.exists():
        print(f"❌ Error: Directory {app_dir} already exists")
        return
    
    # Copy base template (includes all features, conditionally enabled)
    print("\n📋 Copying base template...")
    base_template = TEMPLATE_DIR / "base"
    if not base_template.exists():
        print(f"❌ Error: Template not found at {base_template}")
        return
    
    shutil.copytree(base_template, app_dir)
    
    # Log enabled features
    for feature in features:
        if feature in FEATURES:
            print(f"  ✓ Enabled: {feature} - {FEATURES[feature]}")
        else:
            print(f"  ⚠️  Unknown feature: {feature}")
    
    # Replace placeholders
    print("\n🔧 Configuring app...")
    replace_placeholders(app_dir, name, features)
    
    # Create pyproject.toml with dependencies
    print("  ✓ Generating pyproject.toml")
    generate_pyproject(app_dir, name, features)
    
    # Create README
    print("  ✓ Generating README.md")
    generate_readme(app_dir, name, features)
    
    print(f"\n✅ App '{name}' generated successfully!")
    print(f"\n📚 Next steps:")
    print(f"  cd {app_dir}")
    print(f"  uv sync                    # Install dependencies")
    print(f"  cp .env.example .env       # Configure environment")
    if "db" in features:
        print(f"  uv run alembic upgrade head  # Run migrations")
    print(f"  uv run uvicorn src.app.main:app --reload")


def replace_placeholders(app_dir: Path, name: str, features: List[str]) -> None:
    """Replace placeholders in all files"""
    placeholders = {
        "{{APP_NAME}}": name,
        "{{APP_TITLE}}": snake_to_title(name.replace("-", "_")),
        "{{HAS_AUTH}}": "True" if "auth" in features else "False",
        "{{HAS_DB}}": "True" if "db" in features else "False",
        "{{HAS_REDIS}}": "True" if "redis" in features else "False",
    }
    
    for root, dirs, files in os.walk(app_dir):
        # Skip venv, .git, __pycache__
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", ".venv", "venv"}]
        
        for file in files:
            if file.endswith((".py", ".md", ".toml", ".yml", ".yaml", ".env.example", ".txt")):
                file_path = Path(root) / file
                try:
                    content = file_path.read_text()
                    for placeholder, value in placeholders.items():
                        content = content.replace(placeholder, value)
                    file_path.write_text(content)
                except Exception as e:
                    print(f"  ⚠️  Could not process {file}: {e}")


def generate_pyproject(app_dir: Path, name: str, features: List[str]) -> None:
    """Generate pyproject.toml with appropriate dependencies"""
    
    base_deps = [
        '"fastapi>=0.115.0"',
        '"uvicorn[standard]>=0.32.0"',
        '"pydantic>=2.9.0"',
        '"pydantic-settings>=2.6.0"',
        '"python-multipart>=0.0.17"',
        '"httpx>=0.27.0"',
    ]
    
    feature_deps = {
        "auth": [
            '"python-jose[cryptography]>=3.3.0"',
            '"passlib[bcrypt]>=1.7.4"',
        ],
        "db": [
            '"sqlalchemy[asyncio]>=2.0.36"',
            '"asyncpg>=0.30.0"',
            '"alembic>=1.14.0"',
        ],
        "redis": [
            '"redis[hiredis]>=5.2.0"',
        ],
        "stripe": [
            '"stripe>=11.2.0"',
        ],
        "celery": [
            '"celery[redis]>=5.4.0"',
        ],
    }
    
    dev_deps = [
        '"pytest>=8.3.0"',
        '"pytest-asyncio>=0.24.0"',
        '"pytest-cov>=6.0.0"',
        '"httpx>=0.27.0"',
        '"ruff>=0.8.0"',
        '"mypy>=1.13.0"',
    ]
    
    all_deps = base_deps[:]
    for feature in features:
        if feature in feature_deps:
            all_deps.extend(feature_deps[feature])
    
    pyproject_content = f'''[project]
name = "{name}"
version = "0.1.0"
description = "Production FastAPI application"
requires-python = ">=3.12"
dependencies = [
    {",\n    ".join(all_deps)}
]

[project.optional-dependencies]
dev = [
    {",\n    ".join(dev_deps)}
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]
ignore = []

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "--cov=src --cov-report=term-missing"
'''
    
    (app_dir / "pyproject.toml").write_text(pyproject_content)


def generate_readme(app_dir: Path, name: str, features: List[str]) -> None:
    """Generate comprehensive README"""
    
    title = snake_to_title(name.replace("-", "_"))
    features_list = "\n".join(f"- ✅ {FEATURES[f]}" for f in features if f in FEATURES)
    
    readme_content = f'''# {title}

Production-ready FastAPI application generated with **ClawHub Pro**.

## Features

{features_list}
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
docker build -t {name} .
docker run -p 8000:8000 --env-file .env {name}
```

---

Generated with ❤️ by [ClawHub Pro](https://clawhubpro.com)
'''
    
    (app_dir / "README.md").write_text(readme_content)


def main():
    parser = argparse.ArgumentParser(
        description="Generate production-ready FastAPI applications"
    )
    parser.add_argument("--name", required=True, help="Application name")
    parser.add_argument(
        "--features",
        help=f"Features: {', '.join(FEATURES.keys())}",
        default="auth,db"
    )
    parser.add_argument("--output", default=".", help="Output directory")
    
    args = parser.parse_args()
    
    features = [f.strip() for f in args.features.split(",") if f.strip()]
    output_dir = Path(args.output).resolve()
    
    generate_app(args.name, features, output_dir)


if __name__ == "__main__":
    main()
