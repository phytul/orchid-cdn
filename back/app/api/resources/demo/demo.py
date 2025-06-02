from flask_restful import Resource
from flasgger import swag_from


class Demo(Resource):
    @swag_from("demo_get.yml")
    def get(self):
        return {
            "success": True,
            "message": "Get succeed!",
            "data": None,
        }, 200

    @swag_from("demo_post.yml")
    def post(self):
        return {
            "success": True,
            "message": "Post succeed!",
            "data": None,
        }, 200
