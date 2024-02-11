from app import app, db
from flask import jsonify, request
from app.controllers import create_item, get_all_items, get_item, update_item, delete_item
from app.models import Item

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(get_all_items())

@app.route('/items/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    return jsonify(get_item(item_id))

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    return jsonify(create_item(data))

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_single_item(item_id):
    data = request.get_json()
    return jsonify(update_item(item_id, data))

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_single_item(item_id):
    return jsonify(delete_item(item_id))