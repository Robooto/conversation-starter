import random

from fastapi import APIRouter
from app.models.topics import Topic

router = APIRouter()

conversation_list_db = {
    'weird': [
        'If your mind were an island, what would it look like?',
        'What flavor of ice cream do you wish existed?',
        'If you had a personal mascot, what would your mascot be?'
    ],
    'random': [
        'What was the last funny video you saw?',
        'What do you do to get rid of stress?',
        'What is something you are obsessed with?',
        'What three words best describe you?'
    ]
}


@router.get("/{topic}")
async def get_conversation_starters(topic: Topic):
    return random.choice(conversation_list_db[topic])
