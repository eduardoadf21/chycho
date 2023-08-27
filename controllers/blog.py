from flask import Flask
from chycho.db import get_database


from flask import (
    Blueprint, render_template
)

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route("/", methods=['GET'])
def index():

    chychoVault = get_database()
    posts = chychoVault["posts2"]
    post_details = posts.find()

    posts = []
    for post in post_details:
        posts.append(post)

    return render_template('index.html', posts=posts[:100:-1])