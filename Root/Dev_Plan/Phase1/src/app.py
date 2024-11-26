from flask import Flask, render_template, jsonify
from config import Config
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_app(config_class=Config):
    """Create and configure the Flask application.

    This function initializes the Flask app with the specified configuration,
    sets up logging, registers blueprints, and defines error handlers.

    Args:
        config_class: The configuration class to use for the app.

    Returns:
        A configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Note: Ensure that the secret key is securely generated and kept secret in production.
    app.secret_key = 'your_secret_key_here'  # TODO: Replace with a secure key for production

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    app.logger = logging.getLogger(__name__)

    # Register blueprints after environment variables are loaded
    from chat.routes import chat_bp
    app.register_blueprint(chat_bp)

    # Error handler should be registered after app creation
    @app.errorhandler(Exception)
    def handle_exception(e):
        """Handle uncaught exceptions and return a JSON error response.

        This ensures that the client receives a consistent error structure.

        Args:
            e: The exception that was raised.

        Returns:
            A tuple containing the JSON error response and the HTTP status code.
        """
        app.logger.error(f"Unhandled exception: {e}")
        response = {
            "error": "An internal error occurred."
        }
        return jsonify(response), 500

    @app.route('/')
    def home():
        """Render the home page of the application."""
        return render_template('index.html')

    # The '/test' route has been removed as it's no longer needed.
    # If you need to add new routes, ensure they do not conflict with existing ones.

    return app

if __name__ == '__main__':
    # Run the app only if this file is executed directly.
    # In production, use a WSGI server like Gunicorn or uWSGI.
    app = create_app()
    app.run(debug=True, port=5001)
