from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.shared import User
from uuid import UUID

router = APIRouter(prefix="/trust", tags=["trust"])


@router.get("/{user_id}")
def get_user_trust_profile(user_id: UUID, session: Session = Depends(get_session)):
    """Get user profile with rating and order count - shared validation endpoint"""
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Placeholder for order count - would need to query orders table
    order_count = 0
    
    return {
        "id": str(user.id),
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role.value,
        "rating": user.rating,
        "is_verified": user.is_verified,
        "order_count": order_count
    }
