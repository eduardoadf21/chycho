from flask import Flask
from chycho.vault import postRepository
from chycho.controllers.auth import login_required

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

    return render_template('index.html', posts=posts[0:8], popular=getPopular())


@bp.route("/<id>/", methods=['POST','GET'])
def getPost(id):

    if request.method == 'POST':
        search_query = request.form['search_query']
        queried_posts = Posts.searchPosts(search_query)
        return render_template('search_results.html', posts=queried_posts, popular=getPopular())

    post = Posts.getPostById(id)

    return render_template('post.html', post=post, popular=getPopular())

@bp.route("/<tag>", methods=['POST','GET'])
def getSpecialPost(tag):

    if request.method == 'POST':
        search_query = request.form['search_query']
        queried_posts = Posts.searchPosts(search_query)
        return render_template('search_results.html', posts=queried_posts)

    post = Posts.getPostByTag(tag)

    return render_template('post.html', post=post, popular=getPopular())

@bp.route("/index/<tag>", methods=['POST','GET'])
def getPostsByTag(tag):

    if request.method == 'POST':
        search_query = request.form['search_query']
        queried_posts = Posts.searchPosts(search_query)
        return render_template('search_results.html', posts=queried_posts)

    posts = Posts.searchPostsByTag(tag)

    return render_template('search_results.html', posts=posts, popular=getPopular())
    
@bp.route("/newPost", methods=['POST','GET'])
@login_required
def newPost():

    if request.method == 'POST':
        
        title = request.form['title']
        tags = request.form.getlist('tags')
        body = request.form['ckeditor']
        tag = request.form['tag'] 
        Posts.newPost(title,body,tag,tags)
        return redirect(url_for('blog.index'))

    return render_template('new_post.html')

@bp.route('/vault', methods=['POST','GET'])
def vault():
    select = request.form.get('tag')
    if select is not None:
        print(select)
        return redirect(url_for('blog.getPostsByTag', tag=select))

    return render_template('vault.html')

@bp.route('/edit/<id>/', methods=['POST','GET'])
@login_required
def editPost(id):
    post = Posts.getPostById(id)


    article_body = post['body']


    if request.method == 'POST':
        tags = request.form.getlist('tags')
        tag = request.form['tag']
        body = request.form['ckeditor']
        Posts.updatePost(id,body,tag,tags)
        print(tags)

        return redirect(url_for('blog.getPost', id=id))

    return render_template('edit_post.html', article_body=article_body)

def getPopular():
    posts = Posts.searchPostsByTag("popular")

    return posts 


