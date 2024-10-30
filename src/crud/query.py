from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.query import Query
from schemas.query import QueryDB

from .base import CRUDBase


class CRUDQuery(CRUDBase):
    """CRUD для работы с моделью Query."""

    async def get_query_by_cad_num(
        self,
        cad_num: str,
        session: AsyncSession,
    ) -> QueryDB:
        """CRUD для получения истории по кадастровому номеру."""
        db_query_cad_num = await session.execute(
            select(Query).where(
                Query.cad_num == cad_num,
            ),
        )
        return db_query_cad_num.scalars().first()


query_crud = CRUDQuery(Query)
