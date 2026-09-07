from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from domain.types import DestinationType
from infrastructure.database.base import BaseModel


class DestinationModel(BaseModel):
    __tablename__ = "destinations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    external_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    bot_account_id: Mapped[int] = mapped_column(
        ForeignKey("bot_accounts.id"),
        nullable=True,
    )

    type: Mapped[DestinationType] = mapped_column(
        Enum(DestinationType),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )
