from pydantic import BaseModel


class QueryCreate(BaseModel):
    """Схема для создания объекта Query."""

    cad_num: str
    longitude: str
    latitude: str
