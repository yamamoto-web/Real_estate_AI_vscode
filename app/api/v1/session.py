from fastapi import APIRouter
from app.models.session import SessionStartResponse, QuestionPayload, AnswerResponse
from app.services.session_service import start_new_session, process_question

router = APIRouter()

@router.post("/start", response_model=SessionStartResponse)
def start_session():
    return start_new_session()

@router.post("/question", response_model=AnswerResponse)
def ask_question(payload: QuestionPayload):
    return process_question(payload)
