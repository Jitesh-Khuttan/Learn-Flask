from flask_restful import Resource, reqparse
from code.models.user import UserModel

class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Please provide the username")
    parser.add_argument('password', type=str, required=True, help="Please provide the password.")

    def post(self):
        request_data = RegisterUser.parser.parse_args()
        username, password = request_data['username'], request_data['password']

        print(UserModel.find_by_username(username))

        if UserModel.find_by_username(username):
            return {"message": f"{username} already exists."}

        try:
            user = UserModel(username=username, password=password)
            user.register()
            return {"message" : f"{username} successfully registered."}, 201
        except Exception:
            return {"message": f"Failed to register."}, 400

    def get(self):
        all_users = UserModel.find_all()
        return [user.to_json() for user in all_users]
