import os


from flask import (
    Blueprint, request, session, send_from_directory, jsonify
)

bp = Blueprint('index', __name__, url_prefix='/')

from flask import Flask


@bp.route("/")
def hello_world():
    return "<p>Chycho!</p>"