from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/ping", response_class=JSONResponse)
async def check_ping(request: Request) -> JSONResponse:
    """Проверяем доступность сервера."""
    return {"server": "OK!"}
