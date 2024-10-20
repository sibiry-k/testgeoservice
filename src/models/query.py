from sqlalchemy import (
    Boolean,
    Column,
    String,
)

from core.db import Base


class Query(Base):
    """Модель запроса."""

    cad_num = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    response = Column(Boolean, nullable=True)
