from flask import Blueprint, request, jsonify, current_app
import openai
import os
from dotenv import load_dotenv
import logging

chat_bp = Blueprint('chat', __name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    logging.error("OpenAI API key not found in environment variables.")

# Initialize OpenAI client with the API key
client = openai.Client(api_key=openai_api_key)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided.'}), 400

    try:
        # Prepare the parameters for the chat completion
        params = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7
        }

        # Call the Chat Completion API using the new client
        completion = client.chat.completions.create(**params)

        # Extract the assistant's reply
        ai_response = completion.choices[0].message.content.strip()

        return jsonify({'response': ai_response})

    except openai.OpenAIError as e:
        # Handle OpenAI API errors
        current_app.logger.error(f"OpenAI API error: {e}")
        return jsonify({'error': 'Failed to process the request with OpenAI.'}), 500

    except Exception as e:
        # Handle unexpected errors
        current_app.logger.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500 