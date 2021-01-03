from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Question)
async def create_question(question: schemas.Question, db: Session = Depends(get_db)):
    db_topic = crud.get_topic_by_id(db, topic_id=question.topic_id)
    if not db_topic:
        raise HTTPException(status_code=400, detail="Topic does not exist")
    return crud.create_question(db=db, question=question, topic=db_topic.topic)


@router.get("/roulette")
async def get_random_question(db: Session = Depends(get_db)):
    return crud.get_random_question(db)


@router.get("/{topic}")
async def get_questions_by_topic(topic: str, roulette: bool = False, db: Session = Depends(get_db)):
    db_topic = crud.get_topic(db, topic=topic)
    if not db_topic:
        raise HTTPException(status_code=400, detail="Topic does not exist")

    return crud.get_questions_by_topic(db, topic_id=db_topic.id, roulette=roulette)
