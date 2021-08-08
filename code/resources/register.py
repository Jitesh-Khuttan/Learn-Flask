from flask_restful import Resource, reqparse
from code.models.user import UserModel
import logging
logging.basicConfig(level=2)

class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Please provide the username")
    parser.add_argument('password', type=str, required=True, help="Please provide the password.")

    def post(self):
        request_data = RegisterUser.parser.parse_args()
        username = request_data['username']

        if UserModel.find_by_username(username):
            return {"message": f"{username} already exists."}

        try:
            UserModel(**request_data).register()
            return {"message": f"{username} successfully registered."}, 201
        except Exception as exp:
            logging.error(f"{exp}")
            return {"message": f"Failed to register."}, 400

    def get(self):
        return {"users": [user.to_json() for user in UserModel.find_all()]}
