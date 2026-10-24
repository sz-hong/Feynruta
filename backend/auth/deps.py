from typing import Annotated
from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .tokens import get_user

bearer = HTTPBearer()

async def get_current_user(
    cred: Annotated[HTTPAuthorizationCredentials, Depends(bearer)],
) -> str:
    username = await get_user(cred.credentials)
    if not username:
        raise HTTPException(
            status_code=401,
            detail="UNAUTHORIZED"
        )
    return username