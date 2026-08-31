from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class BatchCreate(BaseModel):
    flock_size: int
    breed: str
    age_weeks: int


class BatchUpdate(BaseModel):
    status: Optional[str] = None
    age_weeks: Optional[int] = None


class BatchResponse(BaseModel):
    id: UUID
    farmer_id: UUID
    flock_size: int
    breed: str
    age_weeks: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class ForecastCreate(BaseModel):
    target_slaughter_age_weeks: int
    feed_conversion_ratio: float = 1.8


class ForecastResponse(BaseModel):
    id: UUID
    batch_id: UUID
    weekly_feed_kg: float
    total_feed_kg: float
    weeks_remaining: int
    created_at: datetime

    class Config:
        from_attributes = True