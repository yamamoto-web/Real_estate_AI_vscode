from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 中間結果を保存（簡易）
last_result = {"response": ""}

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "response": last_result["response"]})

@app.post("/submit")
def handle_submit(answer: str = Form(...)):
    # 簡単な処理（例：大文字にする）
    processed = f"あなたの答え：{answer.upper()}"
    last_result["response"] = processed
    return {"message": "受け取りました"}
