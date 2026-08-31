from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class SupplierListing(SQLModel, table=True):
    __tablename__ = "supplier_listings"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    supplier_id: UUID = Field(foreign_key="users.id")
    product_name: str
    quantity_available: float
    price_per_unit: float


class PooledOrder(SQLModel, table=True):
    __tablename__ = "pooled_orders"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    listing_id: UUID = Field(foreign_key="supplier_listings.id")
    buyer_id: UUID = Field(foreign_key="users.id")
    quantity_requested: float
