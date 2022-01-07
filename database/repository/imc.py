import sqlite3

from database.query.query_imc import query_imc
from database.session import connect_to_db

def value(imc: dict) -> float:
    imc_value = imc['weight']/(imc['height']**2)
    return round(imc_value,2)

def get_imc():
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMCS)
        rows = cur.fetchall()

        # convert row objects to dictionary
        imcs = [dict(row) for row in rows]

    except:
        imcs = []

    return imcs

def get_imc_by_id(imc_id):
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query_imc.GET_IMC_BY_ID, (imc_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        imc = dict(row)
    except:
        imc = {}

    return imc

def insert_imc(imc):
    inserted_imc = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            query_imc.INSERT_IMC,
            (
                imc['birthday'],
                imc['height'], 
                imc['weight'], 
                value(imc),
                imc['user']
            )
        )
        conn.commit()
        inserted_imc = get_imc_by_id(cur.lastrowid)

    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_imc

def update_imc(imc_update, imc_id):
    imc = get_imc_by_id(imc_id)
    if not imc:
        return {}
    imc = {**imc, **imc_update}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            query_imc.UPDATE_IMC_BY_ID,
            (
                imc['birthday'],
                imc['height'], 
                imc['weight'], 
                value(imc),
                imc['user']
            )
        )
        conn.commit()

        #return the user
        updated_imc = get_imc_by_id(user["imc_id"])

    except:
        conn.rollback()
        updated_imc = {}
    finally:
        conn.close()

    return updated_imc

def delete_imc(imc_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute(
            query_imc.DELETE_IMC_BY_ID, 
            (imc_id,)
        )
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message
