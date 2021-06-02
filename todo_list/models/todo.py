from peewee import Model, TextField, DateTimeField
from datetime import datetime
from marshmallow import Schema, fields


class Todo(Model):
    content = TextField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super(Todo, self).save(*args, **kwargs)


class TodoSchema(Schema):
    id = fields.Integer()
    content = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


todo_schema = TodoSchema()
