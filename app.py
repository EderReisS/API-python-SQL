from flask import Flask
from flask_cors import CORS


from database.session import create_db_table, create_db_table_imc

from api.v1.api_imcs import imc_app
from api.v1.api_users import user_app

create_db_table()
create_db_table_imc()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(imc_app)
app.register_blueprint(user_app)


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)