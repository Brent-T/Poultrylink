from fastapi import APIRouter, Depends, HTTPException, Header
from app.core.security import decode_access_token

router = APIRouter(prefix="/market-link", tags=["market_link"])


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


@router.get("/matches")
def get_matches(current_user: dict = Depends(get_current_user)):
    """Get all buyer-farmer matches"""
    return {"matches": [], "message": "Placeholder - implement matches"}


@router.post("/matches")
def create_match(match_data: dict, current_user: dict = Depends(get_current_user)):
    """Create a new buyer-farmer match"""
    return {"message": "Placeholder - implement match creation", "match": match_data}
