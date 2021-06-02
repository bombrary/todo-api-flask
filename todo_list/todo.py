from flask import Blueprint, request

bp = Blueprint('todo', __name__)


@bp.route('/', methods=["GET"])
def get_all():
    return 'get_all'


@bp.route('/', methods=["POST"])
def post():
    body = request.get_json()
    return f'post: {body}'


@bp.route('/<int:todo_id>/', methods=["GET"])
def get(todo_id: int):
    return f'get: {todo_id}'


@bp.route('/<int:todo_id>/', methods=["PUT"])
def put(todo_id: int):
    body = request.get_json()
    return f'put: {todo_id}, {body}'


@bp.route('/<int:todo_id>/', methods=["DELETE"])
def delete(todo_id: int):
    return f'delete: {todo_id}'
