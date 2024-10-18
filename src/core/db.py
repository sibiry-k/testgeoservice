from datetime import datetime as dt

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

from core.config import settings


class PreBase:
    """Расширене базового класса для моделей."""

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=dt.now, nullable=False)
    updated_at = Column(DateTime, onupdate=dt.now)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.db_url)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncSession:
    """Получение асинхронной сессии для работы с SQLAlchemy."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
