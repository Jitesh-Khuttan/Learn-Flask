from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from user import UserDB
from items import ItemDB

all_items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', required=True, type=float)

    def get(self, name):
        item = ItemDB.find_by_name(item_name=name)
        if item:
            ret_val = {"name": item.name, "price": item.price}
            return {"item": ret_val}, 200
        return {"message": f"Item '{name}' not found."}, 400

    def post(self, name):
        request_data = Item.parser.parse_args()
        if ItemDB.find_by_name(item_name=name):
            return {"item": None, "message": f"Item '{name}' already exists."}, 400

        ItemDB.add_item(item_name=name, item_price=request_data['price'])
        ret_val = {"name": name, "price": request_data["price"]}
        return {"item": ret_val}, 201

    def put(self, name):
        request_data = Item.parser.parse_args()
        item = ItemDB.find_by_name(name)
        if item is None:
            ItemDB.add_item(name, request_data['price'])
        else:
            ItemDB.update_item(name, request_data['price'])

        ret_val = {"name": name, "price": request_data["price"]}
        return {"item": ret_val}, 201

    @jwt_required()
    def delete(self, name):
        item = ItemDB.delete_item(name)
        if item:
            ret_val = {"name" : item.name, "price" : item.price}
            return {"item" : ret_val}, 200

        return {"message" : f"Item '{name}' not found!"}, 404

class ItemList(Resource):
    def get(self):
        all_items = ItemDB.find_all()
        if all_items:
            all_items = [
                {"name": item.name, "price": item.price} for item in all_items
            ]
            return {"items": all_items}, 200
        return {"items" : []}, 200


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Please provide the username")
    parser.add_argument('password', type=str, required=True, help="Please provide the password.")

    def post(self):
        request_data = RegisterUser.parser.parse_args()
        username, password = request_data['username'], request_data['password']
        if UserDB.find_by_username(username):
            return {"message": f"{username} already exists."}
        try:
            UserDB.register_user(username, password)
            return {"message" : f"{username} successfully registered."}, 201
        except Exception:
            return {"message": f"Failed to register."}, 400



