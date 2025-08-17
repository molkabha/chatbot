from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

api_key = os.getenv("API_KEY")
MODEL = "gemini-1.5-flash"  # ممكن تغيرها حسب المتاح

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": user_message}]}]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    try:
        bot_reply = data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        bot_reply = "❌ حصل خطأ، حاول تاني."

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
