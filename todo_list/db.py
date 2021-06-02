from peewee import SqliteDatabase
from .models.todo import Todo
from flask import Flask

db = SqliteDatabase(None)


def init_app(app: Flask):
    db.init(app.config['DB_PATH'])
    db.bind([Todo])
    app.teardown_appcontext(close_db)


def close_db(e=None):
    if db.is_closed():
        db.close()
