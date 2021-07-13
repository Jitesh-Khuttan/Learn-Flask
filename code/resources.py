from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from user import User, UserDB

all_items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', required=True, type=float)

    def get(self, name):
        item = next(filter(lambda x: x["name"].upper() == name.upper(), all_items), None)
        return {"item": item}, 200 if item else 400

    def post(self, name):
        request_data = Item.parser.parse_args()
        if next(filter(lambda x: x["name"].upper() == name.upper(), all_items), None) is not None:
            return {"item": None, "message": f"Item '{name}' already exists."}, 400
        new_item = {'name': name, 'price': request_data['price']}
        all_items.append(new_item)
        return {"item": new_item}, 201

    def put(self, name):
        request_data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"].upper() == name.upper(), all_items), None)
        if item is None:
            new_item = {'name': name, 'price': request_data['price']}
            all_items.append(new_item)
            return {"item": new_item}, 201

        item.update(request_data)
        return {"item": item}, 201

    @jwt_required()
    def delete(self, name):
        del_index = [idx for idx, item in enumerate(all_items) if item['name'].upper() == name.upper()]
        if del_index:
            deleted_item = all_items.pop(del_index[0])
            return {"item": deleted_item}, 200
        return {"item": None}, 404


class ItemList(Resource):
    def get(self):
        return {"items": all_items}


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



