from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()

# 環境変数にOpenAI APIキーを設定しておくこと（例：.envファイルなど）
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ChatGPT APIを呼び出す処理
def ask_chatgpt(question: str, history: list) -> str:
    try:
        # 過去履歴をmessagesに追加
        messages = [{"role": "system", "content": "あなたは不動産アドバイザーです。"}]

        # 履歴をuser/assistantのペアで追加
        for h in history:
            messages.append({"role": "user", "content": h["question"]})
            messages.append({"role": "assistant", "content": h["answer"]})

        # 今回の質問を追加
        messages.append({"role": "user", "content": question})

        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        answer = response.choices[0].message.content

        # 正規表現で「おすすめ地域: ...」を抽出
        match = re.search(r"おすすめ地域:\s*([^\n]+)", answer)
        recommended_area = match.group(1).strip() if match else "不明"

        return {
            "answer": answer,
            "recommended_area": recommended_area
        }
    except Exception as e:
        return f"エラーが発生しました: {e}"
    
def get_final_recommendation(history: list) -> dict:
    try:
        messages = [{"role": "system", "content": (
            "あなたは不動産アドバイザーです。"
            "これまでのユーザとの会話履歴を踏まえて、最適な居住地域を3件まで提案してください。"
            "回答は簡潔に、最後に必ず次の形式で出力してください："
            "「おすすめ地域: ○○市, △△町, □□区」"
        )}]

        for h in history:
            messages.append({"role": "user", "content": h["question"]})
            messages.append({"role": "assistant", "content": h["answer"]})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        final_answer = response.choices[0].message.content

        # ✅ 正規表現で地域部分を抽出
        match = re.search(r"おすすめ地域:\s*([^\n]+)", final_answer)
        recommended_area = match.group(1).strip() if match else "不明"

        return {
            "answer": final_answer,
            "recommended_area": recommended_area
        }
    except Exception as e:
            return f"エラーが発生しました: {e}"
