import os
from flask import Flask
from flask_ckeditor import CKEditor

ckeditor = CKEditor()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    ckeditor.init_app(app)
    app.config.from_mapping(
        SECRET_KEY='dev'
        #DATABASE=os.path.join(app.instance_path, 'api.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #from . import db
    #db.init_app(app)

    from chycho.controllers import blog
    app.register_blueprint(blog.bp)
    
    from chycho.controllers import auth
    app.register_blueprint(auth.bp)

    return app
