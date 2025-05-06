from flask import Blueprint

bp = Blueprint('/my-space', __name__, url_prefix='/my-space')


@bp.route('/')
def my_space():
    return 'My Space'
