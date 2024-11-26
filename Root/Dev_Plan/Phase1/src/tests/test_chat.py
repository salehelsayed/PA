import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from flask import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['OPENAI_API_KEY'] = 'your_openai_api_key'  # Ensure API key is set
    client = app.test_client()

    yield client

def test_send_valid_message(client):
    response = client.post('/chat', json={'message': 'Hello, how are you?'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'response' in data
    assert len(data['response']) > 0

def test_empty_message_submission(client):
    response = client.post('/chat', json={'message': ''})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'No message provided.'

def test_excessive_message_length(client):
    long_message = 'a' * 10000  # Message of 10,000 'a's
    response = client.post('/chat', json={'message': long_message})
    data = response.get_json()
    assert response.status_code == 200
    assert 'response' in data

def test_maximum_allowed_characters(client):
    max_length_message = 'a' * 500  # Assuming 500 is the limit
    response = client.post('/chat', json={'message': max_length_message})
    data = response.get_json()
    assert response.status_code == 200
    assert 'response' in data 