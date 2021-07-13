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
    db_name = 'users.db'
    table_name = 'users(id INTEGER PRIMARY KEY, username text, password text)'
    create_table(db_name, table_name)
