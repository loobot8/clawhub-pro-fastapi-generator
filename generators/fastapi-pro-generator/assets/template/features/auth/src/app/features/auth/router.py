"""Authentication router"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from app.core.security import create_access_token, get_current_user, verify_password, hash_password


router = APIRouter(prefix="/auth")


class LoginRequest(BaseModel):
    """Login credentials"""
    username: str
    password: str


class TokenResponse(BaseModel):
    """JWT token response"""
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """Current user response"""
    id: str
    username: str
    roles: list[str]


@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest):
    """Authenticate user and return JWT token"""
    
    # TODO: Replace with actual user lookup from database
    # This is a demo implementation
    if credentials.username == "demo" and credentials.password == "demo123":
        access_token = create_access_token(
            data={"sub": "demo-user-id", "roles": ["user"]}
        )
        return TokenResponse(access_token=access_token)
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    """Get current authenticated user"""
    return UserResponse(
        id=current_user["id"],
        username="demo",  # TODO: Get from database
        roles=current_user["roles"],
    )
