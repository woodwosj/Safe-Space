from flask import Flask
from flask_socketio import SocketIO
from config import Config

socketio = SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    socketio.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    return app
