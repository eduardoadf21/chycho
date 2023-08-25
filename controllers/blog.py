import os
from flask import Flask


from flask import (
    Blueprint, render_template
)

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html')