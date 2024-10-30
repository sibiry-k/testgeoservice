from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Схема получения User."""

    pass


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания User."""

    pass


class UserUpdate(schemas.BaseUserUpdate):
    """Схема обновления для User."""

    pass
