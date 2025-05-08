# app.py
# Flask app (API endpoints, chatbot integration)

from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response

# Initialize the Flask app
app = Flask(__name__)

# Route: Home Page (renders chatbot UI)
@app.route('/')
def index():
    return render_template('index.html')  # Chat interface

# Route: Chatbot API - receives user message, returns bot reply
@app.route('/get-response', methods=['POST'])
def get_response():
    try:
        # Get user message from frontend (sent via JavaScript)
        user_message = request.json.get("message")

        # Validate message
        if not user_message:
            return jsonify({"reply": "Please enter a message."})

        # Get chatbot's reply using chatbot.py logic
        bot_reply = get_bot_response(user_message)

        # Return chatbot reply to frontend
        return jsonify({"reply": bot_reply})
    
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

# Optional: Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Smart EduBot is running!"})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
