from peewee import Model, TextField, DateTimeField, DoesNotExist
from datetime import datetime
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import NotFound, BadRequest


class Todo(Model):
    content = TextField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField()

    @classmethod
    def get_or_404(cls, todo_id: int):
        try:
            todo = Todo.get(Todo.id == todo_id)
        except DoesNotExist:
            raise NotFound
        return todo

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super(Todo, self).save(*args, **kwargs)


class TodoSchema(Schema):
    id = fields.Integer()
    content = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


todo_schema = TodoSchema()


def dump_todo(obj, many=False):
    return todo_schema.dump(obj, many=many)


def load_todo_or_400(obj):
    try:
        return todo_schema.load(obj)
    except ValidationError:
        raise BadRequest
