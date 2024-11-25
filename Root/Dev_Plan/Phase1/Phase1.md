# Phase 1: Simple Text-Based UI with OpenAI Integration

## Goal
Establish a foundational user interface that allows users to input text, sends this input to OpenAI's API, and displays the generated responses.

## Steps

### UI Development

#### Choose Framework
- **Web Interface**: Use Flask for a lightweight local server or React.js for a more dynamic and scalable frontend.

#### Design Interface
Create a clean and intuitive interface with:
- A text input field for user queries
- A display area for showing responses from OpenAI
- Basic navigation elements if needed

### Backend Integration

#### Set Up Server
- If using Flask, set up routes to handle incoming requests from the frontend

#### Connect to OpenAI API
- Implement API calls to OpenAI's GPT-4 (or relevant model) to send user inputs and receive responses
- Ensure secure handling of API keys and manage rate limits

### Output Handling

#### Display Responses
- Render the plain text responses from OpenAI in the UI
- Optionally, support Markdown rendering for better formatting using libraries like marked.js (for React) or Python-Markdown (for Flask)

#### Basic Error Handling
- Implement error messages for failed API calls or invalid inputs
- Provide user feedback for loading states during API interactions

### Tools
- **Frontend**: Flask or React.js
- **Backend**: Python (with Flask) or Node.js (for React.js backend)
- **API Integration**: OpenAI Python SDK or relevant HTTP client
- **Styling**: CSS frameworks like Bootstrap or Tailwind CSS for a responsive design


# Output
Modern Web Interface:
Clean, responsive design using Bootstrap
Real-time chat interface with message bubbles
Support for markdown rendering in AI responses
Fixed input area at the bottom for easy typing
Backend Features:
Flask server handling requests
OpenAI API integration for generating responses
Environment-based configuration for API keys
Error handling for API calls and user input
Security Features:
API key stored in .env file (not in code)
Input validation
Error handling for failed API calls

# The enhanced version now includes:

System Message:
A predefined SYSTEM_MESSAGE that guides the AI's behavior
Sets expectations for response format and style
Conversation History:
Uses Flask sessions to maintain conversation history
Each conversation starts with the system message
Keeps track of both user inputs and AI responses
Context Management:
Maintains the last 10 messages to keep the context window manageable
Includes the full conversation history in each API call
Preserves conversation flow and context between messages
Session Management:
Uses Flask's session to persist conversation history
Initializes new conversations with the system message
Manages conversation state per user