from flask_restplus import fields


class Models:
    def __init__(self, api):
        status = api.model('Status', {
            'code': fields.Integer, 
            'message': fields.String,
            'records': fields.Integer})

        self.books_data = api.model('BookData', {
            'title': fields.String, 
            'description': fields.String,
            'subject_headings': fields.String,
            'notes': fields.String,
            'medium': fields.String,
            'isbn': fields.String,
            'physical_location': fields.String,
            'language': fields.List(fields.String),
            'online_format': fields.List(fields.String),
            'additional_meta': fields.String})

        self.books = api.model('Books', {
            'data': fields.List(fields.Nested(self.books_data)),
            'status': fields.Nested(status)})
