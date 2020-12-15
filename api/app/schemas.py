from typing import List, Optional
from pydantic import BaseModel


class Question(BaseModel):
    question: str
    topic_id: int

    class Config:
        orm_mode = True


class TopicBase(BaseModel):
    topic: str


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    questions: List[Question] = []

    class Config:
        orm_mode = True
