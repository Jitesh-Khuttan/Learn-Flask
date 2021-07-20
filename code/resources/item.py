from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from code.models.items import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', required=True, type=float)

    def get(self, name):
        item = ItemModel.find_by_name(item_name=name)
        if item:
            return {"item": item.to_json()}, 200
        return {"message": f"Item '{name}' not found."}, 400

    def post(self, name):
        request_data = Item.parser.parse_args()
        if ItemModel.find_by_name(item_name=name):
            return {"message": f"Item '{name}' already exists."}, 400

        item = ItemModel(name=name, price=request_data['price'])
        item.save_to_db()
        return {"item": item.to_json()}, 201

    def put(self, name):
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(item_name=name)
        if item:
            item.price = request_data['price']
        else:
            item = ItemModel(name=name, price=request_data['price'])

        item.save_to_db()
        return {"item": item.to_json()}, 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(item_name=name)
        if item:
            item.delete_from_db()
            return {"item": item.to_json()}, 200

        return {"message": f"Item '{name}' not found!"}, 404


class ItemList(Resource):
    def get(self):
        result = []
        all_items = ItemModel.find_all()
        if all_items:
            result = [item.to_json()for item in all_items]
        return {"items": result}, 200
