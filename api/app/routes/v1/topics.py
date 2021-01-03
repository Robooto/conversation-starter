from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.get("/")
async def get_topics(db: Session = Depends(get_db)):
    return crud.get_topics(db)


@router.post("/", response_model=schemas.Topic)
async def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    db_topic = crud.get_topic(db, topic=topic.topic)
    if db_topic:
        raise HTTPException(status_code=400, detail="Topic already exists")
    return crud.create_topic(db=db, topic=topic)
