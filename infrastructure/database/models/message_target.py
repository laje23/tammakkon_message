from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from domain.types.message_target_status import MessageTargetStatusType
from infrastructure.database.base import Base


class MessageTargetModel(Base):
    __tablename__ = "message_targets"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    message_id: Mapped[int] = mapped_column(
        ForeignKey("messages.id"),
        nullable=False,
    )

    destination_id: Mapped[int] = mapped_column(
        ForeignKey("destinations.id"),
        nullable=False,
    )

    status: Mapped[MessageTargetStatusType] = mapped_column(
        Enum(MessageTargetStatusType),
        nullable=False,
    )

    retry_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    last_error: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    send_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )
