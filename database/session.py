import sqlite3

from database.query.query_user import query_user
from database.query.query_imc import query_imc     


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute(query_user.CREATE_TABLE_USERS)
        conn.commit()
        print(">>> User table created successfully")
    except:
        print(">>> User table creation failed - Maybe table")
    finally:
        conn.close()

def create_db_table_imc():
    try:
        conn = connect_to_db()
        conn.execute(query_imc.CREATE_TABLE_IMC)
        conn.commit()
        print(">>> IMC table created successfully")
    except:
        print(">>> IMC table creation failed - Maybe table")
    finally:
        conn.close()
