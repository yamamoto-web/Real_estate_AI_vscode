FROM python:3.11-slim
WORKDIR /app

# uvicorn は必須なので先に入れておく
RUN pip install --no-cache-dir uvicorn

# 依存リストをコピー & pip install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY . /app

# サーバ起動コマンド
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]