class QueryIMC:
    CREATE_TABLE_IMC: str = """
    CREATE TABLE IF NOT EXISTS imc (
                imc_id INTEGER PRIMARY KEY NOT NULL,
                birthday TEXT NOT NULL,
                height REAL NOT NULL,
                weight REAL NOT NULL,
                imc_value REAL NOT NULL,
                user INTERGER NOT NULL,
                FOREIGN KEY user REFERENCES users(user_id)  
            );
    """

    INSERT_IMC: str = """
    INSERT INTO imc (birthday, height, weight, imc_value, user) VALUES (?, ?, ?, ?, ?)
    """
    GET_IMC_BY_ID: str = """
    SELECT * FROM imc WHERE user_id = ?
    """
    GET_IMCS: str = """
    SELECT * FROM imc
    """
    UPDATE_IMC_BY_ID: str = """
    UPDATE imc SET birthday = ?, height = ?, weight = ?, imc_value = ?, user = ? WHERE imc_id =?
    """
    DELETE_IMC_BY_ID: str = """
    DELETE from imc WHERE imc_id = ?
    """

query_imc = QueryIMC()