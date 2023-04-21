from fastapi import APIRouter

from src.api.v1.endpoints.user import router as user_router

router = APIRouter()


router.include_router(router=user_router, prefix="/user", tags=["user"])
