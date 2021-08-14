from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from werkzeug.security import safe_str_cmp
from code.models.user import UserModel
import logging
logging.basicConfig(level=2)

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True, help="Please provide the username")
_user_parser.add_argument('password', type=str, required=True, help="Please provide the password.")


class UserRegister(Resource):
    def post(self):
        request_data = _user_parser.parse_args()
        username = request_data['username']

        if UserModel.find_by_username(username):
            return {"message": f"{username} already exists."}

        try:
            UserModel(**request_data).register()
            return {"message": f"{username} successfully registered."}, 201
        except Exception as exp:
            logging.error(f"{exp}")
            return {"message": f"Failed to register."}, 400

class User(Resource):

    def get(self, name):
        user = UserModel.find_by_username(username=name)
        if user:
            return user.to_json()
        return {"message": f"User '{name}' not found!"}, 404

    @jwt_required()
    def delete(self, name):
        user = UserModel.find_by_username(username=name)
        if user:
            user.delete_from_db()
        return {"message": "User deleted!"}


class UserLogin(Resource):

    def post(self):
        request_data = _user_parser.parse_args()
        user = UserModel.find_by_username(username=request_data['username'])
        if user and safe_str_cmp(request_data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {'access_token': access_token, 'refresh_token': refresh_token}

        return {"message": "user not found!"}
