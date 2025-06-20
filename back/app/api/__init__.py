from flask import Blueprint
from flask_restful import Api
from app.api.resources.demo.demo import Demo

api_blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_blueprint)

api.add_resource(Demo, "/demo")
