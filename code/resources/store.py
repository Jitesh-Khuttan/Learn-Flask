import logging
from flask_restful import Resource
from code.models.store import StoreModel

class Store(Resource):

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"Store '{name}' already exists."}
        store = StoreModel(name=name)
        try:
            store.save_to_db()
        except Exception as exp:
            logging.error(str(exp))
            return {'message': "Failed to create the store."}, 500

        return store.to_json(), 201

    def get(self, name):
        store = StoreModel.find_by_name(store_name=name)
        if store:
            return store.to_json(), 200
        return {'message': f"Store '{name}' not found!"}, 404

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted.'}


class StoreList(Resource):

    def get(self):
        return {'stores': [store.to_json() for store in StoreModel.get_all()]}
