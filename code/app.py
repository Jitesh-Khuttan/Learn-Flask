from flask import Flask
from flask_restful import Api
from resources import Item, ItemList, RegisterUser
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-important-key'
jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')

app.run(port=9000)
