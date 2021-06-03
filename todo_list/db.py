from peewee import SqliteDatabase
from .models.todo import Todo
from flask import Flask
from flask.cli import with_appcontext
import click

db = SqliteDatabase(None)


def init_app(app: Flask):
    db.init(app.config['DB_PATH'])
    db.bind([Todo])
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def close_db(e=None):
    if not db.is_closed():
        db.close()


def init_db():
    db.connect()
    db.drop_tables([Todo])
    db.create_tables([Todo])
    db.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
