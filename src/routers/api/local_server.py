from fastapi import APIRouter, BackgroundTasks, Depends, Request
from fastapi.responses import JSONResponse
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.db import get_async_session
from core.user import current_user
from crud.query import query_crud
from models.query import Query
from schemas.query import QueryCreate, QueryDB

router = APIRouter()


async def request_to_remote_server(cad_num, session):
    """Запрашиваем информацию на удаленном сервере и обновляем БД."""
    async with AsyncClient() as client:
        response = await client.post(settings.api_url, timeout=60)
        if response.text == '"true"':
            remote_server_response = True
        else:
            remote_server_response = False
        print(cad_num)
        result = await session.execute(
            select(Query).where(Query.cad_num == cad_num),
        )
        obj = result.scalar_one_or_none()
        if obj:
            obj.response = remote_server_response
        await session.commit()
        print(f'Для кадастрового номера {cad_num} получен ответ.')


@router.get("/ping", response_class=JSONResponse)
async def check_ping(request: Request) -> JSONResponse:
    """Проверяем доступность сервера."""
    return {"server": "OK!"}


@router.post(
    '/query',
    response_model=QueryDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)],
    )
async def create_new_query(
    query: QueryCreate,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_async_session),
) -> QueryDB:
    """Создает запись в таблице Query и отправляет запрос на внешний API."""
    Query(
        cad_num=query.cad_num,
        longitude=query.longitude,
        latitude=query.latitude,
    )
    background_tasks.add_task(
        request_to_remote_server,
        cad_num=query.cad_num,
        session=session,
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
