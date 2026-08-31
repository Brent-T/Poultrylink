from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class ProcessorBooking(SQLModel, table=True):
    __tablename__ = "processor_bookings"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    farmer_id: UUID = Field(foreign_key="users.id")
    processor_id: UUID = Field(foreign_key="users.id")
    booking_date: str
    quantity: float
    status: str = Field(default="PENDING")
