from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)

from core.db import Base


class Query(Base):
    """Модель запроса."""

    cad_num = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    response = Column(Boolean, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
