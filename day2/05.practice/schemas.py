from marshmallow import Schema, fields

# dump_only = 서버에서 직접 관리

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)