from flask import Flask
from chycho.db import get_database


from flask import (
    Blueprint, render_template, request, redirect, url_for
)

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route("/", methods=('POST','GET'))
def index():

    chychoVault = get_database()
    posts = chychoVault["posts2"]

    if request.method == 'POST':
        search_query = request.form['search_query']
        query = {"title": { "$regex": search_query }}
        search_results = posts.find(query)
        for post in search_results:
            print(post)
            
    post_details = posts.find()

    posts = []
    for post in post_details:
        posts.append(post)

    return render_template('index2.html', posts=posts[0:4])

@bp.route("/<title>", methods=['GET'])
def getPost(title):

    chychoVault = get_database()
    posts = chychoVault["posts2"]
    post = posts.find_one({"title": title})

    return render_template('post.html', post=post)
