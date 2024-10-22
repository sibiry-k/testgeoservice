from typing import Optional

from pydantic import BaseModel


class QueryBase(BaseModel):
    """Базовая схема для объекта Query."""

    cad_num: str
    longitude: str
    latitude: str


class QueryCreate(QueryBase):
    """Схема для создания объекта Query."""

    pass


class QueryDB(QueryBase):
    """Схема для получения объектов Query."""

    id: int
    response: Optional[bool]

    class Config:
        """Базовая настройка схемы."""

        from_attributes = True
