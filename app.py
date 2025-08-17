from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("API_KEY")
MODEL = "gemini-1.5-flash"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={api_key}"

    payload = {
        "contents": [{"parts": [{"text": user_message}]}]
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        bot_reply = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("Error:", e)
        bot_reply = "❌ حصل خطأ، حاول تاني."

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
