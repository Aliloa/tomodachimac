from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes.users import etudiants_bp
    app.register_blueprint(etudiants_bp)

    return app