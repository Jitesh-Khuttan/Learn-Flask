
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

class UserMapping:
    userid_mapping = {}
    username_mapping = {}

    @staticmethod
    def add_user(User):
        UserMapping.userid_mapping[User.id] = User
        UserMapping.username_mapping[User.username] = User

    @staticmethod
    def get_user_by_id(_id):
        return UserMapping.userid_mapping.get(_id)

    @staticmethod
    def get_user_by_name(username):
        return UserMapping.username_mapping.get(username)

class UserId:
    incremental_id = 0

    @staticmethod
    def get_id():
        UserId.incremental_id += 1
        return UserId.incremental_id
