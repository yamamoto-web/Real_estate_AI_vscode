from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# GET: 初期表示
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

# POST: 入力を受け取って回答を返す
@app.post("/", response_class=HTMLResponse)
async def receive_answer(request: Request, user_input: str = Form(...)):
    response = f"あなたの入力：{user_input} に対する応答です。"
    return templates.TemplateResponse("index.html", {"request": request, "answer": response})
