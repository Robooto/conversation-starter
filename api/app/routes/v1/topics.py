from fastapi import APIRouter

from app.models import Topic

router = APIRouter()


@router.get("/")
async def get_topics():
    return [e.value for e in Topic]
