from code.models.user import UserDB
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    user = UserDB.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(jwt_payload):
    _id = jwt_payload['identity']
    user = UserDB.find_by_id(_id)
    return user if user else None
