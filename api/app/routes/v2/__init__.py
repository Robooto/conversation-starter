from fastapi import APIRouter

from app.routes.v2 import topics, questions

api_router = APIRouter()
api_router.include_router(topics.router, prefix="/topics", tags=["topics"])
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])
