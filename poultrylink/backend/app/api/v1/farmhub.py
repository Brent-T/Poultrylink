from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session
from app.core.database import get_session
from app.core.security import decode_access_token
from app.schemas.farmhub import BatchCreate, BatchUpdate, BatchResponse, ForecastCreate, ForecastResponse
from app.crud import farmhub as farmhub_crud
from uuid import UUID
from typing import List

router = APIRouter(prefix="/farmhub", tags=["FarmHub"])
security = HTTPBearer()



def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/batches", response_model=List[BatchResponse])
def get_batches(
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    farmer_id = UUID(current_user["sub"])
    return farmhub_crud.get_batches_by_farmer(session, farmer_id)


@router.post("/batches", response_model=BatchResponse)
def create_batch(
    batch_data: BatchCreate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    farmer_id = UUID(current_user["sub"])
    return farmhub_crud.create_batch(session, farmer_id, batch_data)


@router.get("/batches/{batch_id}", response_model=BatchResponse)
def get_batch(
    batch_id: UUID,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    batch = farmhub_crud.get_batch_by_id(session, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch


@router.patch("/batches/{batch_id}", response_model=BatchResponse)
def update_batch(
    batch_id: UUID,
    batch_data: BatchUpdate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    batch = farmhub_crud.update_batch(session, batch_id, batch_data)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch


@router.post("/batches/{batch_id}/forecast", response_model=ForecastResponse)
def create_forecast(
    batch_id: UUID,
    forecast_data: ForecastCreate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    batch = farmhub_crud.get_batch_by_id(session, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    
    weeks_remaining = forecast_data.target_slaughter_age_weeks - batch.age_weeks
    if weeks_remaining <= 0:
        raise HTTPException(status_code=400, detail="Target age must be greater than current age")
    
    weekly_feed_kg = round(batch.flock_size * forecast_data.feed_conversion_ratio, 2)
    total_feed_kg = round(weekly_feed_kg * weeks_remaining, 2)

    from uuid import uuid4
    from datetime import datetime
    return ForecastResponse(
        id=uuid4(),
        batch_id=batch_id,
        weekly_feed_kg=weekly_feed_kg,
        total_feed_kg=total_feed_kg,
        weeks_remaining=weeks_remaining,
        created_at=datetime.utcnow()
    )