from flask import Blueprint, request, jsonify
from .db import db
from .models.todo import Todo, dump_todo, load_todo_or_400

bp = Blueprint('todo', __name__)


@bp.before_request
def connect_db():
    db.connect()


@bp.route('/', methods=["GET"])
def get_all():
    todos = list(Todo.select())
    return jsonify(dump_todo(todos, many=True))


@bp.route('/', methods=["POST"])
def post():
    todo_dict = load_todo_or_400(request.get_json())
    todo = Todo.create(content=todo_dict['content'])
    return jsonify(todo.id)


@bp.route('/<int:todo_id>/', methods=["GET"])
def get(todo_id: int):
    todo = Todo.get_or_404(todo_id)
    return jsonify(dump_todo(todo))


@bp.route('/<int:todo_id>/', methods=["PUT"])
def put(todo_id: int):
    todo = Todo.get_or_404(todo_id)
    todo_dict = load_todo_or_400(request.get_json())
    todo.content = todo_dict['content']
    todo.save()
    return jsonify(dict())


@bp.route('/<int:todo_id>/', methods=["DELETE"])
def delete(todo_id: int):
    todo = Todo.get_or_404(todo_id)
    todo.delete_instance()
    return jsonify(dict())
