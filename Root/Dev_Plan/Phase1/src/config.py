import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'your_secret_key_here')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # Add other configuration variables here

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False 