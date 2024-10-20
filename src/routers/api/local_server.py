import httpx
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from core.config import settings
from crud.query import create_query
from models.query import Query
from schemas.query import QueryCreate

router = APIRouter()


@router.get("/ping", response_class=JSONResponse)
async def check_ping(request: Request) -> JSONResponse:
    """Проверяем доступность сервера."""
    return {"server": "OK!"}


@router.post('/query')
async def create_new_query(
    query: QueryCreate,
) -> Query:
    """Создает запись в таблице Query."""
    return await create_query(query)


@router.get('/result')
async def get_result(request: Request) -> JSONResponse:
    """Получает от удаленного сервера результат обработки запроса."""
    api_url = settings.api_url

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()
