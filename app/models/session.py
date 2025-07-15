from pydantic import BaseModel
from typing import List

class SessionStartResponse(BaseModel):
    session_id: str

class QuestionPayload(BaseModel):
    session_id: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    recommended_area: str

class HistoryItem(BaseModel):
    question: str
    answer: str

class ResultResponse(BaseModel):
    session_id: str
    final_answer: str
    recommended_area: str
    history: List[HistoryItem]