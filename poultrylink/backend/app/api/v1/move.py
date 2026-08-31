from fastapi import APIRouter, Depends, HTTPException, Header
from app.core.security import decode_access_token

router = APIRouter(prefix="/move", tags=["move"])


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


@router.get("/deliveries")
def get_deliveries(current_user: dict = Depends(get_current_user)):
    """Get all deliveries"""
    return {"deliveries": [], "message": "Placeholder - implement deliveries"}


@router.post("/deliveries")
def create_delivery(delivery_data: dict, current_user: dict = Depends(get_current_user)):
    """Create a new delivery assignment"""
    return {"message": "Placeholder - implement delivery creation", "delivery": delivery_data}
