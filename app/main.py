from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import openai
from dotenv import load_dotenv
import os

# 環境変数からAPIキーを読み込む
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# フォーム画面（初回アクセス時）を表示
@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

# フォームからPOSTされたデータを処理して応答を返す
@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):
    reply = await ask_chatgpt(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "response": reply})

# ChatGPT APIを呼び出す処理
async def ask_chatgpt(message: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは親切な不動産コンシェルジュです。"},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content.strip()