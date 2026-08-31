from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth, trust, farmhub, supply_market, market_link, process_link, move
from app.core.database import SQLModel, engine

security = HTTPBearer()

app = FastAPI(
    title="PoultryLink API",
    swagger_ui_parameters={"persistAuthorization": True}
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(trust.router, prefix="/api/v1")
app.include_router(farmhub.router, prefix="/api/v1")
app.include_router(supply_market.router, prefix="/api/v1")
app.include_router(market_link.router, prefix="/api/v1")
app.include_router(process_link.router, prefix="/api/v1")
app.include_router(move.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)
