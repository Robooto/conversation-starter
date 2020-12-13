from fastapi import APIRouter

from app.routes.v1 import topics, starters

api_router = APIRouter()
api_router.include_router(topics.router, prefix="/topics", tags=["topics"])
api_router.include_router(starters.router, prefix="/starters", tags=["starters"])