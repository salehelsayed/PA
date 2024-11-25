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

@chat_bp.route('/api/directory', methods=['POST'])
def get_directory():
    data = request.json
    selected_directory = data.get('directory_path')

    allowed_base_directory = '/path/to/allowed/base/directory'  # Set to the allowed base path

    if selected_directory:
        # Resolve the absolute path
        absolute_path = os.path.abspath(selected_directory)
        # Check if the selected directory is within the allowed base directory
        if os.path.commonpath([absolute_path, allowed_base_directory]) != allowed_base_directory:
            return jsonify({'error': 'Access to the specified directory is not allowed.'}), 403
        # Store the selected directory in the session
        session['selected_directory'] = absolute_path

    base_directory = session.get('selected_directory')

    if not base_directory or not os.path.exists(base_directory):
        return jsonify({'error': 'Directory not found.'}), 400

    def get_directory_structure(path):
        structure = []
        try:
            with os.scandir(path) as it:
                for entry in it:
                    if entry.name.startswith('.'):
                        continue  # Skip hidden files and directories
                    if entry.is_dir(follow_symlinks=False):
                        structure.append({
                            'type': 'directory',
                            'name': entry.name,
                            'children': get_directory_structure(os.path.join(path, entry.name))
                        })
                    else:
                        structure.append({
                            'type': 'file',
                            'name': entry.name
                        })
            return structure
        except PermissionError:
            return []

    directory_structure = get_directory_structure(base_directory)
    return jsonify(directory_structure)

@chat_bp.route('/api/file', methods=['GET'])
def read_file():
    file_path = request.args.get('file_path')
    base_directory = session.get('selected_directory')

    if not file_path or not base_directory:
        return jsonify({'error': 'File path not provided.'}), 400

    # Resolve the absolute path
    absolute_path = os.path.abspath(os.path.join(base_directory, file_path))

    # Security check
    if os.path.commonpath([absolute_path, base_directory]) != base_directory:
        return jsonify({'error': 'Access to the specified file is not allowed.'}), 403

    if not os.path.exists(absolute_path):
        return jsonify({'error': 'File not found.'}), 404

    with open(absolute_path, 'r') as file:
        content = file.read()

    return jsonify({'content': content})

# @chat_bp.route('/browse', methods=['GET'])
# def browse():
#     # This route is no longer needed
#     pass 