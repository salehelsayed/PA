from flask import Blueprint, request, jsonify, current_app, session
import openai
import os
from dotenv import load_dotenv
import logging
import json

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

# Comment out or remove the /api/directory endpoint if not needed
# @chat_bp.route('/api/directory', methods=['POST'])
# def get_directory():
#     # Endpoint no longer needed for client-side directory loading
#     pass

@chat_bp.route('/api/file', methods=['GET'])
def read_file():
    file_path = request.args.get('file_path')
    base_directory = session.get('selected_directory')

    if not file_path or not base_directory:
        return jsonify({'error': 'File path not provided.'}), 400

    # Resolve the absolute path
    absolute_path = os.path.abspath(os.path.join(base_directory, file_path))

    # Security check to prevent access outside the base directory
    if not absolute_path.startswith(base_directory):
        return jsonify({'error': 'Access to the specified file is not allowed.'}), 403

    if not os.path.exists(absolute_path):
        return jsonify({'error': 'File not found.'}), 404

    try:
        with open(absolute_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        current_app.logger.error(f"Error reading file {absolute_path}: {e}")
        return jsonify({'error': 'An error occurred while reading the file.'}), 500

    return jsonify({'content': content})

# @chat_bp.route('/browse', methods=['GET'])
# def browse():
#     # This route is no longer needed
#     pass 