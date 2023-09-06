from flask import Flask
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


@bp.route("/<id>/", methods=['POST','GET'])
def getPost(id):

    if request.method == 'POST':
        search_query = request.form['search_query']
        queried_posts = Posts.searchPosts(search_query)
        return render_template('search_results.html', posts=queried_posts)

    post = Posts.getPostById(id)

    return render_template('post.html', post=post)
    
@bp.route("/newPost", methods=['POST','GET'])
def newPost():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['ckeditor']

    return render_template('new_post.html')

@bp.route('/edit/<id>/', methods=['POST','GET'])
def editPost(id):
    post = Posts.getPostById(id)

    article_body = post['body']

    if request.method == 'POST':
        body = request.form['ckeditor']
        Posts.updatePost(id,body)

        return redirect(url_for('blog.getPost', id=id))

    return render_template('edit_post.html', article_body=article_body)


