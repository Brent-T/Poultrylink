from fastapi import APIRouter, Depends, HTTPException, Header
from app.core.security import decode_access_token

router = APIRouter(prefix="/supply-market", tags=["supply_market"])


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


@router.get("/listings")
def get_listings(current_user: dict = Depends(get_current_user)):
    """Get all supplier listings"""
    return {"listings": [], "message": "Placeholder - implement listings"}


@router.post("/listings")
def create_listing(listing_data: dict, current_user: dict = Depends(get_current_user)):
    """Create a new supplier listing"""
    return {"message": "Placeholder - implement listing creation", "listing": listing_data}
