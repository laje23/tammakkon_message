from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from infrastructure.database import BaseModel


class RolePermissionModel(BaseModel):
    __tablename__ = "role_permissions"

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"),
        primary_key=True,
    )

    permission: Mapped[str] = mapped_column(
        String(100),
        primary_key=True,
    )
