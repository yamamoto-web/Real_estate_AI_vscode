# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

from fastapi import FastAPI
from app.api.v1 import session  # sessionルーターを読み込む

app = FastAPI()

# v1のルーター登録
app.include_router(session.router, prefix="/v1/session", tags=["session"])

@app.get("/")
def root():
    return {"message": "API is running"}

# 環境変数からAPIキーを読み込む
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # フォーム画面（初回アクセス時）を表示
# @app.get("/", response_class=HTMLResponse)
# async def form_get(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "response": ""})

# # フォームからPOSTされたデータを処理して応答を返す
# @app.post("/chat", response_class=HTMLResponse)
# async def chat(request: Request, user_input: str = Form(...)):
#     reply = await ask_chatgpt(user_input)
#     return templates.TemplateResponse("index.html", {"request": request, "response": reply})

# ChatGPT APIを呼び出す処理
# async def ask_chatgpt(message: str) -> str:
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "あなたは親切な不動産アドバイザーです。"},
#                 {"role": "user", "content": message}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"エラーが発生しました: {e}"