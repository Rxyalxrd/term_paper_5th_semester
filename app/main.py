from fastapi import FastAPI

from app.core import settings
from app.api.main_router import main_router


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

app.include_router(main_router)