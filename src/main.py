import uvicorn
from fastapi import FastAPI

from core.config import settings
from routers.main_router import main_router


def get_application() -> FastAPI:
    """Базовая настройка приложения."""
    application = FastAPI(
        title=settings.app_title,
        debug=settings.debug_mode,
    )
    application.include_router(main_router)
    return application


app = get_application()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)
