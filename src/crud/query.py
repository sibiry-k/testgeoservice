from core.db import AsyncSessionLocal
from models.query import Query
from schemas.query import QueryCreate


async def create_query(
    new_query: QueryCreate,
) -> Query:
    """CRUD-операция для создания объекта Query."""
    new_query_data = new_query.dict()

    db_query = Query(**new_query_data)

    async with AsyncSessionLocal() as session:
        session.add(db_query)
        await session.commit()
        await session.refresh(db_query)

    return db_query
