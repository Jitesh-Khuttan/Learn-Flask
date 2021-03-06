import os
from flask import Flask
from flask_restful import Api
from code.resources.item import Item, ItemList
from code.resources.store import Store, StoreList
from code.resources.register import RegisterUser
from flask_jwt import JWT
from code.security.security import authenticate, identity
from code.db.alchemy_db import db
from code.db.config import db_dir_path

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-important-key'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{db_dir_path}/data.db")
if os.environ.get('DATABASE_URL') and os.environ.get('DATABASE_URL').startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    "Creates tables if they don't exist."
    db.create_all()

jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__":
    app.run(port=9000)
