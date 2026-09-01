from datetime import datetime

from sqlalchemy import DateTime, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from domain.types import LogCategory, LogLevel
from infrastructure.database.base import Base


class LogModel(Base):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    category: Mapped[LogCategory] = mapped_column(
        Enum(LogCategory),
        nullable=False,
    )

    level: Mapped[LogLevel] = mapped_column(
        Enum(LogLevel),
        nullable=False,
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    source: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

