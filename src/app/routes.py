from flask import Blueprint, request, jsonify, render_template
import requests
from textblob import TextBlob
from src.config.settings import GROQ_API_KEY, GROQ_API_ENDPOINT

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def home():
    """Render the home page."""
    return render_template("index.html")

@routes.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
    """Analyze sentiment using the Groq API."""
    try:
        user_input = request.json.get("user_input")
        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Send request to Groq API
        response = requests.post(
            GROQ_API_ENDPOINT,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "messages": [{"role": "user", "content": user_input}],
                "model": "llama-3.1-8b-instant",  # Update model if needed
            },
        )

        if response.status_code != 200:
            return jsonify({"error": f"Groq API error: {response.text}"}), response.status_code

        # Parse the API response
        response_data = response.json()
        message_content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")

        # Analyze sentiment with TextBlob
        blob = TextBlob(message_content)
        sentiment_score = blob.sentiment.polarity

        # Determine sentiment
        if sentiment_score > 0.1:
            sentiment = "positive 😊"
        elif sentiment_score < -0.1:
            sentiment = "negative 😔"
        elif sentiment_score == 0 :
            sentiment = "neutral ☹️"

        return jsonify({"sentiment": sentiment, "details": message_content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@routes.route("/chat", methods=["POST"])
def chat():
    """Handle chatbot interactions."""
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Example chatbot logic or API call (replace this with your chatbot logic)
        assistant_response = f"You said: {user_message}"

        return jsonify({"response": assistant_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500