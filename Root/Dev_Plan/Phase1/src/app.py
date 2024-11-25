from flask import Flask, render_template, jsonify
from config import Config
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_app(config_class=Config):
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'your_secret_key_here'

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    app.logger = logging.getLogger(__name__)

    # Register blueprints after environment variables are loaded
    from chat.routes import chat_bp
    app.register_blueprint(chat_bp)

    # Error handler should be registered after app creation
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f"Unhandled exception: {e}")
        response = {
            "error": "An internal error occurred."
        }
        return jsonify(response), 500

    @app.route('/')
    def home():
        return render_template('index.html')

    # Remove or comment out the test route
    # @app.route('/test')
    # def test_page():
    #     return render_template('test.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
