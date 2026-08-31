from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.core.security import get_password_hash, create_access_token, decode_access_token, verify_password
from app.models.shared import User, RoleEnum
from app.schemas.auth import UserCreate, UserLogin, TokenResponse, UserResponse
from datetime import timedelta
from app.core.config import settings
from uuid import UUID, uuid4

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    # Check if user already exists
    statement = select(User).where(User.email == user_data.email)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_pw = get_password_hash(user_data.password)
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_pw,
        full_name=user_data.full_name,
        phone=user_data.phone,
        location=user_data.location,
        role=user_data.role
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    # Generate token
    access_token = create_access_token(
        data={"sub": str(new_user.id), "role": new_user.role.value},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=new_user.id,
            email=new_user.email,
            role=new_user.role,
            full_name=new_user.full_name
        )
    )


@router.post("/login", response_model=TokenResponse)
def login(credentials: UserLogin, session: Session = Depends(get_session)):
    statement = select(User).where(User.email == credentials.email)
    user = session.exec(statement).first()
    
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(
        data={"sub": str(user.id), "role": user.role.value},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            email=user.email,
            role=user.role,
            full_name=user.full_name
        )
    )


@router.get("/me", response_model=UserResponse)
def get_current_user_endpoint(
    authorization: str,
    session: Session = Depends(get_session)
):
    try:
        token = authorization.replace("Bearer ", "")
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user_id = UUID(payload.get("sub"))
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserResponse(
            id=user.id,
            email=user.email,
            role=user.role,
            full_name=user.full_name
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
