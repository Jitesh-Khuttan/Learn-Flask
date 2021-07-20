from code.db.alchemy_db import db

class UserModel(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(100))

    def to_json(self):
        return {'id': self.id, 'username': self.username}

    def register(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, userid):
        return cls.query.filter_by(id=userid).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


if __name__ == "__main__":
    user = UserModel(username="jkhuttan", password="asdf")
    print(user.to_json())
