from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class RoleEnum(str, Enum):
    FARMER = "FARMER"
    BUYER = "BUYER"
    SUPPLIER = "SUPPLIER"
    PROCESSOR = "PROCESSOR"
    DRIVER = "DRIVER"


class DeliveryStatusEnum(str, Enum):
    ASSIGNED = "ASSIGNED"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"


class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    full_name: str
    phone: str
    location: str
    role: RoleEnum
    is_verified: bool = Field(default=False)
    rating: float = Field(default=0.0)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Batch(SQLModel, table=True):
    __tablename__ = "batches"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    farmer_id: UUID = Field(foreign_key="users.id")
    flock_size: int
    breed: str
    age_weeks: int
    status: str = Field(default="ACTIVE")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Order(SQLModel, table=True):
    __tablename__ = "orders"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    buyer_id: UUID = Field(foreign_key="users.id")
    seller_id: UUID = Field(foreign_key="users.id")
    batch_id: UUID = Field(foreign_key="batches.id")
    quantity_kg: float
    status: str = Field(default="PENDING")
    total_price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Delivery(SQLModel, table=True):
    __tablename__ = "deliveries"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    order_id: UUID = Field(foreign_key="orders.id")
    driver_id: UUID = Field(foreign_key="users.id")
    status: DeliveryStatusEnum = Field(default=DeliveryStatusEnum.ASSIGNED)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Payment(SQLModel, table=True):
    __tablename__ = "payments"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    order_id: UUID = Field(foreign_key="orders.id")
    amount: float
    method: str
    status: str = Field(default="PENDING")
    created_at: datetime = Field(default_factory=datetime.utcnow)
