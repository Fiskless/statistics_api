import uvicorn as uvicorn
from fastapi import FastAPI

from statistic.handlers import router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = get_application()
