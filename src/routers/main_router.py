from fastapi import APIRouter

from .api import local_router, user_router

main_router = APIRouter()

main_router.include_router(
    local_router,
    prefix='',
    tags=['Local'],
)
main_router.include_router(
    user_router,
)
