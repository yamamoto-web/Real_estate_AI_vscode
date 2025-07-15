from fastapi import HTTPException
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

    answer = f"おすすめの地域は鎌倉市です（あなたの質問: {payload.question}）"
    _sessions[payload.session_id].append({"question": payload.question, "answer": answer})
    return {"answer": answer, "recommended_area": "鎌倉市"}

