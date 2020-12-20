from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal
from app.questions import conversation_list_db


def get_topics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Topics).offset(skip).limit(limit).all()


def get_topic(db: Session, topic: str):
    return db.query(models.Topics).filter(models.Topics.topic == topic).first()


def get_topic_by_id(db: Session, topic_id: int):
    return db.query(models.Topics).filter(models.Topics.id == topic_id).first()


def create_topic(db: Session, topic: schemas.TopicCreate):
    db_topic = models.Topics(topic=topic.topic)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic


def create_question(db: Session, question: schemas.Question, topic: str):
    topic = get_topic(db, topic)
    db_question = models.Questions(question=question.question, topic_id=topic.id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_random_question_by_topic(db: Session, topic_id: int):
    return db.query(models.Questions).filter(models.Questions.topic_id == topic_id).order_by(func.random()).first()


def get_random_question(db: Session):
    return db.query(models.Questions).order_by(func.random()).first()


def seed_db():
    db = SessionLocal()
    try:
        for topic in conversation_list_db:
            db_topic = create_topic(db, topic=schemas.TopicCreate(topic=topic))
            for question in conversation_list_db[topic]:
                create_question(db, schemas.Question(question=question, topic_id=db_topic.id), topic=topic)
        db.close()
    except IntegrityError:
        db.close()
        print('db already seeded')
