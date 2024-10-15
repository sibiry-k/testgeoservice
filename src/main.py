from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def read_root() -> JSONResponse:
    """Получает главную страницу."""
    return {"Hello": "World"}
