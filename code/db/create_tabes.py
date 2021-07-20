from code.db.db_access import DBAccess

def create_table(db_name, table_name):
    db = DBAccess(db_name)
    sql = f"""
        CREATE TABLE {table_name}
    """
    print(sql)
    with db.connect():
        db.execute(sql)

if __name__ == "__main__":
    db_name = 'data.db'
    table_name = 'items(id INTEGER PRIMARY KEY, name text, price real)'
    create_table(db_name, table_name)

    table_name = 'users(id INTEGER PRIMARY KEY, username text, password real)'
    create_table(db_name, table_name)
