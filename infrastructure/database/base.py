from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker , mapped_column , Mapped
from config.setting import settings

engine = create_engine(
    settings.DATABASE_URL if settings.DATABASE_URL else "", echo=True
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