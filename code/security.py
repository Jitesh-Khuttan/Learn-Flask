from user import User, UserMapping, UserId
from werkzeug.security import safe_str_cmp

def register_user(username, password):
    if UserMapping.get_user_by_name(username):
        return f"{username} already exists."

    user = User(_id=UserId.get_id(), username=username, password=password)
    UserMapping.add_user(user)
    return f"{username} registered."


def authenticate(username, password):
    user = UserMapping.get_user_by_name(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(jwt_payload):
    _id = jwt_payload['identity']
    user = UserMapping.get_user_by_id(_id)
    return True if user else False
