from app import app, db
from flask import jsonify, request
from app.controllers import register_user, register_all_user, get_register_user, update_register_user, delete_register_user
from app.models import tbl_user


@app.route('/user', methods=['GET', 'POST'])
def regi_user_and_list():
    if request.method == 'POST':
        data = request.get_json()
        return register_user(data)
    else:
        return jsonify(register_all_user())

@app.route('/user/<int:user_id>', methods=['GET', 'POST', 'DELETE'])
def update_get_delete_regi_user(user_id):
    if request.method == 'POST':
        data = request.get_json()
        return jsonify(update_register_user(user_id, data))
    elif request.method == 'DELETE':  # Adding an elif condition for DELETE method
        return jsonify(delete_register_user(user_id))
    else:
        return jsonify(get_register_user(user_id))