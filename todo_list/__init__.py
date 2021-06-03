from flask import Flask
import os


def make_instance_path(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def create_app(test_config: dict = None):
    app = Flask(__name__)
    app.config['DB_PATH'] = os.path.join(app.instance_path, 'db.sqlite3')
    app.config['JSON_AS_ASCII'] = False

    if test_config is not None:
        app.config.from_mapping(test_config)

    make_instance_path(app)

    from . import db
    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello, World'

    from . import todo
    app.register_blueprint(todo.bp, url_prefix="/todo")

    return app
