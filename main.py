from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api

from auto_utils import log
from auto_mongo import MongoCRUD
from kbss_books_models import Models

app = Flask(__name__)
api = Api(app, title='KBSS Book Service')
CORS(app)

# dao = MongoCRUD('books', 'kbss_assets')
model = Models(api)


@api.route('/books')
class Alerts(Resource):
    @api.marshal_with(model.books)
    def get(self):
        # return dao.read({}, collection='books', db='kbss_assets')
        return {'data': {'book': {'id': 1,
                                      'title': 'Haiti a Choisi de Devenir un Pays Pauve',
                                      'author': 'Etzer Emile',
                                      'isbn': '01780e0f41166cdf765db519d6480fcff9de7e38'}},
                    'status': {'code': '200',
                               'message': 'OK'}}
    
    @api.expect(model.books_data)
    def post(self):
        pass

    @api.expect(model.books_data)
    def put(self):
        pass


if __name__ == '__main__':
    app.run()
