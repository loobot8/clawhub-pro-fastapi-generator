# AUTH FEATURE ADDITIONS TO CONFIG.PY
# This file extends the base config when auth feature is enabled

    # Auth
    jwt_secret: SecretStr  # Required
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30
