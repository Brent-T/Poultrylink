from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID


class FeedRecord(SQLModel, table=True):
    __tablename__ = "feed_records"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    batch_id: UUID = Field(foreign_key="batches.id")
    feed_type: str
    quantity_kg: float
    date: str


class BatchForecast(SQLModel, table=True):
    __tablename__ = "batch_forecasts"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    batch_id: UUID = Field(foreign_key="batches.id")
    predicted_weight: float
    predicted_date: str
