from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

# 个人空间
@bp.route('/personal-space')
def my_space():
    return render_template('personal-space.html')
