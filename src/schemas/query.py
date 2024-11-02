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


class QueryUpdate(QueryBase):
    """Схема для обновления объекта Query."""

    response: bool


class QueryDB(QueryBase):
    """Схема для получения объектов Query."""

    id: int
    user_id: Optional[int]
    response: Optional[bool] = None

    class Config:
        """Базовая настройка схемы."""

        from_attributes = True
