from sqlalchemy import ForeignKey, Table, Column

from infrastructure.database.base import BaseModel

user_role_table = Table(
    "user_roles",
    BaseModel.metadata,
    Column(
        "user_id",
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "role_id",
        ForeignKey("roles.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
