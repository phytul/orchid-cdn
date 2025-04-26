from flask import Flask
from app.my_space import my_space_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(my_space_bp)

    return app
