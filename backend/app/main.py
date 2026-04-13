from datetime import timedelta

from fastapi import FastAPI, HTTPException, status
from jose import JWTError

from app.auth import (
    ACCESS_TOKEN_EXPIRE_SECONDS,
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_username_from_refresh_token,
)
from app.models import LoginRequest, RefreshRequest, Token

app = FastAPI(title="JWT Authentication API", version="1.0.0")


@app.post("/token", response_model=Token, summary="Obtain JWT tokens")
def login(credentials: LoginRequest):
    """
    Authenticate with username and password and receive an access token
    (valid for 300 seconds) and a refresh token (valid for 24 hours).
    """
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS),
    )
    refresh_token = create_refresh_token(data={"sub": user["username"]})
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
    )


@app.post("/token/refresh", response_model=Token, summary="Refresh JWT tokens")
def refresh_token(body: RefreshRequest):
    """
    Provide a valid refresh token to obtain a new access token and a new
    refresh token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username = get_username_from_refresh_token(body.refresh_token)
    except JWTError:
        raise credentials_exception

    access_token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS),
    )
    new_refresh_token = create_refresh_token(data={"sub": username})
    return Token(
        access_token=access_token,
        refresh_token=new_refresh_token,
        token_type="bearer",
    )
