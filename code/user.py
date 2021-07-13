from code.db.db_access import DBAccess

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

class UserDB:
    db_name, table_name = 'users.db', 'users'
    db = DBAccess(db_name)

    @classmethod
    def register_user(cls, username, password):
        query = f"""
            INSERT INTO {cls.table_name} VALUES (NULL, ?, ?)
        """
        params = (username, password)
        with cls.db.connect():
            cls.db.execute(sql=query, params=params, commit=True)

    @classmethod
    def find_by_username(cls, username):
        query = f"""
            SELECT * FROM {cls.table_name} WHERE username = (?)
        """
        params = (username, )
        with cls.db.connect():
            result = cls.db.retrieve(sql=query, params=params, fetchall=False)
            user = User(*result)
            return user

    @classmethod
    def find_by_id(cls, userid):
        query = f"""
            SELECT * FROM {cls.table_name} WHERE id = (?)
        """
        params = (userid, )
        with cls.db.connect():
            result = cls.db.retrieve(sql=query, params=params, fetchall=False)
            user = User(*result)
            return user

if __name__ == "__main__":
    # user = User('jkhuttan', 'asdf')
    # UserDB.register_user(user)
    result = UserDB.find_by_username('hkhuttan')
    print(result)
    result = UserDB.find_by_id(1)
    print(result)
