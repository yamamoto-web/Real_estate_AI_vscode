from fastapi import HTTPException
from app.services.chatgpt_service import ask_chatgpt
from app.services.chatgpt_service import get_final_recommendation
import uuid

# メモリ上でセッション管理（将来DBに移行可能）
_sessions = {}

def start_new_session():
    session_id = str(uuid.uuid4())
    _sessions[session_id] = []
    return {"session_id": session_id}

def process_question(payload):
    if payload.session_id not in _sessions:
        raise HTTPException(status_code=400, detail="Invalid session_id")
    
    history = _sessions[payload.session_id]
    result  = ask_chatgpt(payload.question, history)

    # 履歴にはフル回答を保存
    _sessions[payload.session_id].append({"question": payload.question, "answer": result["answer"]})

    return {
        "answer": result["answer"],
        "recommended_area": result["recommended_area"]
    }

def get_session_result(session_id: str):
    if session_id not in _sessions:
        raise HTTPException(status_code=400, detail="Invalid session_id")

    history = _sessions[session_id]
    final_result = get_final_recommendation(history)
    
    return {
        "session_id": session_id,
        "final_answer": final_result["answer"],
        "recommended_area": final_result["recommended_area"],
        "history": history
    }