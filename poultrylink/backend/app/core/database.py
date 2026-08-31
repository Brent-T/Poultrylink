from sqlmodel import SQLModel, create_engine
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.ENVIRONMENT == "development"
)


def get_session():
    session = engine.connect()
    try:
        yield session
    finally:
        session.close()
