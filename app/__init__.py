from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__ , template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    from .routes import main
    from .auth import auth
    from .ws import socketio_events

    app.register_blueprint(main)
    app.register_blueprint(auth)

    socketio_events(socketio)

    return app
