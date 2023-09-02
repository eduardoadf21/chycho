from flask import Flask
from chycho.db import get_database
from chycho.vault import postRepository


from flask import (
    Blueprint, render_template, request, redirect, url_for
)

bp = Blueprint('blog', __name__, url_prefix='/')

Posts = postRepository()

@bp.route("/", methods=['POST','GET'])
def index():

    if request.method == 'POST':
        search_query = request.form['search_query']
        queried_posts = Posts.searchPosts(search_query)
        return render_template('search_results.html', posts=queried_posts)
            
    posts = Posts.getPosts()

    return render_template('index.html', posts=posts[0:4])


@bp.route("/<title>", methods=['POST','GET'])
def getPost(title):

    if request.method == 'POST':
        search_query = request.form['search_query']
        queried_posts = Posts.searchPosts(search_query)
        return render_template('search_results.html', posts=queried_posts)

    post = Posts.getPostByTitle(title)

    return render_template('post.html', post=post)
