from pydantic import BaseModel

class SessionStartResponse(BaseModel):
    session_id: str

class QuestionPayload(BaseModel):
    session_id: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    recommended_area: str
