from typing import List
from pydantic import BaseModel, ConfigDict, Field


class Question(BaseModel):
    question: str
    topic_id: int

    model_config = ConfigDict(from_attributes=True)


class TopicBase(BaseModel):
    topic: str


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    questions: List[Question] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
