from code.db.alchemy_db import db

class ItemModel(db.Model):

    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #'stores' is a table name here.
    store = db.relationship('StoreModel')

    def to_json(self):
        return {'name': self.name, 'price': self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, item_name):
        return cls.query.filter_by(name=item_name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


if __name__ == "__main__":
    item = ItemModel(name='Pizza', price=150.79)
    print(item.to_json())
