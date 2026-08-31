from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class DeliveryAssignment(SQLModel, table=True):
    __tablename__ = "delivery_assignments"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    order_id: UUID = Field(foreign_key="orders.id")
    driver_id: UUID = Field(foreign_key="users.id")
    status: str = Field(default="ASSIGNED")
    pickup_location: str
    dropoff_location: str
