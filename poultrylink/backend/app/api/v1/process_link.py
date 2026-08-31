from fastapi import APIRouter, Depends, HTTPException, Header
from app.core.security import decode_access_token

router = APIRouter(prefix="/process-link", tags=["process_link"])


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


@router.get("/bookings")
def get_bookings(current_user: dict = Depends(get_current_user)):
    """Get all processor bookings"""
    return {"bookings": [], "message": "Placeholder - implement bookings"}


@router.post("/bookings")
def create_booking(booking_data: dict, current_user: dict = Depends(get_current_user)):
    """Create a new processor booking"""
    return {"message": "Placeholder - implement booking creation", "booking": booking_data}
