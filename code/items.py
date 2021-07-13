from code.db.db_access import DBAccess

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemDB:
    db_name, table_name = 'items.db', 'items'
    db = DBAccess(db_name)

    @classmethod
    def add_item(cls, item_name, item_price):
        query = """
            INSERT into items VALUES (?, ?)
        """
        params = (item_name, item_price)
        with cls.db.connect():
            cls.db.execute(query, params, commit=True)

    @classmethod
    def update_item(cls, item_name, item_price):
        query = """
            UPDATE items SET price = ? WHERE name = ?
        """
        params = (item_price, item_name)
        with cls.db.connect():
            cls.db.execute(query, params, commit=True)

    @classmethod
    def delete_item(cls, item_name):
        query = """
            DELETE from items WHERE name = ?
        """
        params = (item_name, )
        item = cls.find_by_name(item_name)
        if item:
            with cls.db.connect():
                cls.db.execute(query, params, commit=True)
                return item

    @classmethod
    def find_by_name(cls, item_name):
        query = """
            SELECT * FROM items WHERE name = ?
        """
        params = (item_name, )
        with cls.db.connect():
            result = cls.db.retrieve(query, params, fetchall=False)
            if result:
                return Item(*result)

    @classmethod
    def find_all(cls):
        query = """
            SELECT * FROM items
        """
        with cls.db.connect():
            result = cls.db.retrieve(query, fetchall=True)
            if result:
                return [Item(*r) for r in result]

