from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../frontend', template_folder='../templates')
    app.config.from_object(config_class)

    db.init_app(app)

    from backend.routes import main, assessment
    app.register_blueprint(main.bp)
    app.register_blueprint(assessment.bp)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app