import random

from fastapi import APIRouter

from app.db.init_db import conversation_list_db
from app.models.topics import Topic

router = APIRouter()


@router.get("/roulette")
async def get_random_starter():
    return random.choice(conversation_list_db[random.choice([e.value for e in Topic])])


@router.get("/{topic}")
async def get_conversation_starters(topic: Topic):
    return random.choice(conversation_list_db[topic])
