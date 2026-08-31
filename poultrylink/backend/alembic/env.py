# Alembic Config file

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import os
from dotenv import load_dotenv

load_dotenv()

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here for 'autogenerate' support
from sqlmodel import SQLModel
from app.models.shared import User, Batch, Order, Delivery, Payment  # noqa
from app.models.farmhub import FeedRecord, BatchForecast  # noqa
from app.models.supply_market import SupplierListing, PooledOrder  # noqa
from app.models.market_link import MarketMatch  # noqa
from app.models.process_link import ProcessorBooking  # noqa
from app.models.move import DeliveryAssignment  # noqa

target_metadata = SQLModel.metadata


def get_url():
    return os.getenv("DATABASE_URL")


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
