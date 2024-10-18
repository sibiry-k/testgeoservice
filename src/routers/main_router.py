from fastapi import APIRouter

from .endpoints import local_router

main_router = APIRouter()

main_router.include_router(
    local_router,
    prefix='',
    tags=['Local'],
)
