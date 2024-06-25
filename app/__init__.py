# app/__init__.py

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

# Create instances of Flask extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login = LoginManager()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login.init_app(app)
    cors.init_app(app, resources={r"/auth/*": {"origins": "http://localhost:3000"}})
    
    # Register blueprints
    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Import models to ensure they are registered with SQLAlchemy
    from app.models.user import User
    
    # Configure Flask-Login user loader
    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

# Import models to ensure they are registered with SQLAlchemy
from app import models
