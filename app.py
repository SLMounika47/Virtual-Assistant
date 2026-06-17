from flask import Flask, render_template, request, jsonify
from datetime import datetime
import time

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data["message"].lower()

    if "hello" in message or "hi" in message:
        reply = "Hello! How can I help you today?"

    elif "how are you" in message:
        reply = "I am doing great. Thank you for asking."

    elif "your name" in message:
        reply = "I am your AI Virtual Assistant."

    elif "python" in message:
        reply = "Python is a powerful programming language used in AI, automation, data science, and web development."

    elif "html" in message:
        reply = "HTML is the standard language used to create web pages."

    elif "css" in message:
        reply = "CSS is used to style and design websites."

    elif "javascript" in message:
        reply = "JavaScript adds interactivity and dynamic behavior to websites."

    elif "flask" in message:
        reply = "Flask is a lightweight Python framework used for web applications."

    elif "ai" in message:
        reply = "Artificial Intelligence allows machines to learn, reason, and solve problems."

    elif "time" in message:
        reply = f"Current time is {datetime.now().strftime('%I:%M %p')}"

    elif "date" in message:
        reply = f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    else:
        reply = f"You asked: {message}. I am a basic AI assistant. To answer everything like ChatGPT, I need an AI API integration."

    time.sleep(1.5)

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)