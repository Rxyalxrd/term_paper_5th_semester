from fastapi import APIRouter

from app.api.endpoints import convert_router


main_router = APIRouter()

main_router.include_router(
    convert_router,
    prefix="/convert_router",
    tags=("Convert router",)
)