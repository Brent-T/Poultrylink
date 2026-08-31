from sqlmodel import Session, select
from app.models.shared import Batch
from app.schemas.farmhub import BatchCreate, BatchUpdate
from uuid import UUID, uuid4
from datetime import datetime


def get_batches_by_farmer(session: Session, farmer_id: UUID):
    statement = select(Batch).where(Batch.farmer_id == farmer_id)
    return session.exec(statement).all()


def get_batch_by_id(session: Session, batch_id: UUID):
    return session.get(Batch, batch_id)


def create_batch(session: Session, farmer_id: UUID, batch_data: BatchCreate):
    batch = Batch(
        id=uuid4(),
        farmer_id=farmer_id,
        flock_size=batch_data.flock_size,
        breed=batch_data.breed,
        age_weeks=batch_data.age_weeks,
        status="ACTIVE",
        created_at=datetime.utcnow()
    )
    session.add(batch)
    session.commit()
    session.refresh(batch)
    return batch


def update_batch(session: Session, batch_id: UUID, batch_data: BatchUpdate):
    batch = session.get(Batch, batch_id)
    if not batch:
        return None
    if batch_data.status:
        batch.status = batch_data.status
    if batch_data.age_weeks:
        batch.age_weeks = batch_data.age_weeks
    session.add(batch)
    session.commit()
    session.refresh(batch)
    return batch