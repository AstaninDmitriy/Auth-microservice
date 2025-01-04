import uuid
import sqlalchemy
from sqlalchemy import DateTime, func, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import (DeclarativeBase, Mapped, declarative_mixin, mapped_column)


metadata = sqlalchemy.MetaData()

@declarative_mixin
class UUIDixin:
    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )


@declarative_mixin
class TimestampMixin:
    created_at: Mapped[str] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
    )
    updated_at: Mapped[str] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(),
    )


class Base(TimestampMixin, UUIDixin, DeclarativeBase):
    metadata = metadata


class Users(Base):
    __tablename__ = "users"
    phone_number: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]