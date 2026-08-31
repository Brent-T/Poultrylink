from fastapi import APIRouter, Depends, HTTPException, Header
from typing import List
from app.core.security import decode_access_token
from uuid import UUID, uuid4

router = APIRouter(prefix="/farmhub", tags=["farmhub"])


def get_current_user(authorization: str = Header(...)):
    """Dependency to get current user from JWT token"""
    try:
        token = authorization.replace("Bearer ", "")
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/batches")
def get_batches(current_user: dict = Depends(get_current_user)):
    """Get all batches for the current farmer"""
    return {"batches": [], "message": "Placeholder - implement batch listing"}


@router.post("/batches")
def create_batch(batch_data: dict, current_user: dict = Depends(get_current_user)):
    """Create a new batch record"""
    return {"message": "Placeholder - implement batch creation", "batch": batch_data}
