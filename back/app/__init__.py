import os

from flask import Flask
from app.config import ProdConfig, DevConfig
from flasgger import Swagger
from app.api import api_blueprint

dict_config = {
    "development": DevConfig,
    "production": ProdConfig,
}


def create_app(options):
    app = Flask(__name__)
    options = dict_config[options["env"]]
    app.config.from_object(options)

    os.environ["FLASK_DEBUG"] = "1" if options.DEBUG else "0"

    app.register_blueprint(api_blueprint)

    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config["title"] = options.SWAGGER_TITLE
    swagger_config["description"] = options.SWAGGER_DESC
    swagger_config["host"] = options.SWAGGER_HOST

    Swagger(app, config=swagger_config)

    return app
