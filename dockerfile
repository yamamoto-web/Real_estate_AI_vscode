# 1. ベースイメージは軽量な Python 3.11
FROM python:3.11-slim

# 2. 作業ディレクトリ
WORKDIR /app

# 3. Poetry をインストール
RUN pip install --no-cache-dir poetry==2.1.3

# 4. ローカルの pyproject.toml, poetry.lock をコピー
COPY pyproject.toml poetry.lock /app/

# 5. 依存をインストール（仮想環境はコンテナ内で完結）
RUN poetry env use python3.11 \
 && poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

# 6. アプリソースをコピー
COPY . /app

# 7. 環境変数の読み込み用
ENV PYTHONUNBUFFERED=1

# 8. uvicorn をシステム経由で使えるようにする
RUN pip install --no-cache-dir uvicorn

# 9. FastAPI を起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]