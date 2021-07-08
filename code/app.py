from flask import Flask
from flask_restful import Resource, Api
from resources import Item, ItemList, RegisterUser, Authorization
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-important-key'
jwt = JWTManager(app)

api = Api(app)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')
api.add_resource(Authorization, '/authorize')

app.run(port=9000)
