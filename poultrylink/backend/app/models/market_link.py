from sqlmodel import SQLModel, Field
from uuid import UUID


class MarketMatch(SQLModel, table=True):
    __tablename__ = "market_matches"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    buyer_id: UUID = Field(foreign_key="users.id")
    farmer_id: UUID = Field(foreign_key="users.id")
    match_score: float
    status: str = Field(default="PENDING")
