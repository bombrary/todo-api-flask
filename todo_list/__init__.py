from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config['DB_PATH'] = os.path.join(app.instance_path, 'db.sqlite3')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello, World'

    from . import todo
    app.register_blueprint(todo.bp, url_prefix="/todo")

    return app
