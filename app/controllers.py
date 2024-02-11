from app import db
from app.models import tbl_user
from flask import request, jsonify

def register_user(data):
    new_user = tbl_user(
        name=data['name'],
        phone_number=data['phone_number'],
        username=data['username']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

def register_all_user():
    users = tbl_user.query.all()
    return [{'id': user.id, 'name': user.name, 'description': user.description} for user in users]

def get_register_user(user_id):
    user = tbl_user.query.get(user_id)
    if user:
        return {'id': user.id, 'name': user.name, 'description': user.description}
    return {'message': 'User not found'}, 404

def update_register_user(user_id, data):
    user = tbl_user.query.get(user_id)
    if user:
        user.name = data.get('name', user.name)
        user.description = data.get('description', user.description)
        db.session.commit()
        return {'message': 'User updated successfully'}
    return {'message': 'User not found'}, 404

def delete_register_user(user_id):
    user = tbl_user.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}
    return {'message': 'User not found'}, 404