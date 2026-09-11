from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker , mapped_column , Mapped
from config import secrets



engine = create_engine(
        secrets.database_url , echo=True
)

sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )