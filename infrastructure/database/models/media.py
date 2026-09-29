from datetime import datetime

from domain.types import MediaType
from sqlalchemy import DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.base import BaseModel


class MediaModel(BaseModel):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    original_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    
    media_type: Mapped[MediaType] = mapped_column(
        Enum(MediaType),
        nullable=False,
    )

    stored_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    size: Mapped[int] = mapped_column(
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
