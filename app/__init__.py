import os

from flask import Flask
from app.routes import main_bp
from config import ProdConfig, DevConfig

dict_config = {
    "development": DevConfig,
    "production": ProdConfig,
}

def create_app(options):
    app = Flask(__name__)
    options = dict_config[options['env']]
    app.config.from_object(options)

    os.environ["FLASK_DEBUG"] = '1' if options.DEBUG else '0'

    app.register_blueprint(main_bp)

    return app
