import random

import uvicorn
from fastapi import FastAPI


def get_application() -> FastAPI:
    """Базовая настройка приложения."""
    return FastAPI(
        title='Remote_Server',
        debug=True,
    )


app = get_application()


@app.get("/result")
async def result() -> str:
    """Отвечает рандомно true или false."""
    result = ['true', 'false']
    return random.choice(result)


if __name__ == '__main__':
    uvicorn.run('remote_main:app', host='0.0.0.0', port=9000, reload=True)
