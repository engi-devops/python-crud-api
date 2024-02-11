from app import app, db
from flask import jsonify, request
from app.controllers import register_user, register_all_user, get_register_user, update_register_user, delete_register_user
from app.models import tbl_user


@app.route('/user', methods=['POST'])
def regi_user():
    data = request.get_json()
    return register_user(data)
    
@app.route('/user', methods=['GET'])
def register_all_user():
    return jsonify(register_all_user())

@app.route('/user/<int:user_id>', methods=['GET'])
def get_register_user(user_id):
    return jsonify(get_register_user(user_id))

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_register_user(user_id):
    data = request.get_json()
    return jsonify(update_register_user(user_id, data))

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_register_user(user_id):
    return jsonify(delete_register_user(user_id))