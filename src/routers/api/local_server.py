import httpx
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.db import get_async_session
from crud.query import query_crud
from models.query import Query
from schemas.query import QueryCreate, QueryDB

router = APIRouter()


@router.get("/ping", response_class=JSONResponse)
async def check_ping(request: Request) -> JSONResponse:
    """Проверяем доступность сервера."""
    return {"server": "OK!"}


@router.post(
    '/query',
    response_model=QueryDB,
    response_model_exclude_none=True,
    )
async def create_new_query(
    query: QueryCreate,
    session: AsyncSession = Depends(get_async_session),
) -> QueryDB:
    """Создает запись в таблице Query и отправляет запрос на внешний API."""
    Query(
        cud_num=query.cad_num,
        longitude=query.longitude,
        latitude=query.latitude,
        response='true',
    )
    async with httpx.AsyncClient() as client:

        response = await client.get(settings.api_url)
        print(response)
        query = Query(
            response='true',
        )
        return await query_crud.create(query, session)


@router.get(
    '/history/',
    response_model=list[QueryDB],
    response_model_exclude_none=True,
)
async def get_history(
    session: AsyncSession = Depends(get_async_session),
) -> QueryDB:
    """Получение списка всех записей модели Query в БД."""
    return await query_crud.get_all(session)


@router.get(
    '/history/{cad_num}',
    response_model=QueryDB,
    response_model_exclude_none=True,
)
async def get_history_by_cad_num(
    cad_num: str,
    session: AsyncSession = Depends(get_async_session),
) -> QueryDB:
    """Получение истории по кадастровому номеру."""
    return await query_crud.get_query_by_cad_num(cad_num, session)
