import os
from flask import Flask, got_request_exception
from flask_cors import CORS
from flask_restful import Api
from mongoengine import connect

from .restaurant import RestaurantApi, RestaurantListApi


def create_flask_app(test=False):
    app = Flask(__name__)
    CORS(app)
    app.config['TESTING'] = test
    # print is here to shut the mouth of linter and check effective connection
    mongo_connection = connect(
        'restaurant_backend' if test else 'restaurant_backend_test',
        host=[os.environ['MONGO_HOST']],
        username=os.environ['MONGO_USERNAME'],
        password=os.environ['MONGO_PASSWORD'],
        authentication_source='admin',
    )

    api = Api(app)
    api.add_resource(RestaurantListApi, '/list')
    api.add_resource(RestaurantApi, '/', '/<string:restaurant_name>')
    return app


app = create_flask_app()

if __name__ == '__main__':
    app.run(debug=True)
