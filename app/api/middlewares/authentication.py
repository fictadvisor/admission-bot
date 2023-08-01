from fastapi import status, HTTPException, Security
from fastapi.security import APIKeyHeader

from app.settings import settings

auth_header = APIKeyHeader(name="Authorization", scheme_name="Bearer", description="Token", auto_error=False)


async def verify_token(token: str = Security(auth_header)):
    if token != f"Bearer {settings.AAPI_TOKEN.get_secret_value()}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return token