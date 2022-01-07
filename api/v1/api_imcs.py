from flask import Blueprint, request, jsonify
from database.repository import imc

imc_app = Blueprint('imc_app',__name__)

from database.repository.imc import get_imc, get_imc_by_id, insert_imc, update_imc, delete_imc
from database.session import create_db_table, create_db_table_imc

create_db_table()
create_db_table_imc()

@imc_app.route('/api/v1/imcs', methods = ['GET'])
def api_get_imcs():
    return jsonify(get_imc())

@imc_app.route('/api/v1/imcs/<imc_id>')
def api_get_imc_by_id(imc_id):
    return jsonify(get_imc_by_id(imc_id))

@imc_app.route('/api/v1/imcs', methods = ['POST'])
def api_insert_imc():
    imc = request.get_json()
    return jsonify(insert_imc(imc))

@imc_app.route('/api/v1/imcs/<imc_id>', methods = ['PATCH'])
def api_update_imc(imc_id):
    return jsonify(update_imc(imc_id))

@imc_app.route('/api/v1/imcs/<imc_id>', methods = ['DELETE'])
def api_delete_imc(imc_id):
    return jsonify(delete_imc(imc_id))

