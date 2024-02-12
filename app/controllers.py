from app import db
from app.models import tbl_user
from flask import jsonify

def register_user(data):
    existing_phone = tbl_user.query.filter_by(phone_number=data['phone_number']).first()
    if existing_phone:
        return jsonify({'Success': False, 'Message': 'User with this phone number already exists.'}), 400
    try:
        new_user = tbl_user(
            name=data['name'],
            phone_number=data['phone_number'],
            username=data['username']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'Success': True, 'Message': 'User created successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'Success': False, 'Message': str(e)}), 400

def register_all_user():
    try:
        users = tbl_user.query.all()
        user_list = [{'id': user.id, 'name': user.name, 'phone_number': user.phone_number, 'username': user.username} for user in users]
        return {'Success': True, 'Message': 'Ok', 'data' : user_list}  # Returning a list of dictionaries
    except Exception as e:
        return {'Success': False, 'Message': str(e)}  # Returning an error message

def get_register_user(user_id):
    try:
        user = tbl_user.query.filter_by(id=user_id).first()
        if user:
            return jsonify({'Success': True, 'Message': 'Ok', 'data' : {'id': user.id, 'name': user.name, 'username': user.username}})
        return jsonify({'Message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'Success': False, 'Message': str(e)}), 400


def update_register_user(user_id, data):
    try:
        user = tbl_user.query.filter_by(id=user_id).first()
        if user:
            user.name = data.get('name', user.name)
            db.session.commit()
            return jsonify({'Success': True, 'Message': 'User updated successfully.'})
        return jsonify({'Success': False, 'Message': 'User not found.'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'Success': False, 'Message': str(e)}), 400

def delete_register_user(user_id):
    try:
        user = tbl_user.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'Success': True, 'Message': 'User deleted successfully.'})
        return jsonify({'Success': False, 'Message': 'User not found.'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'Success': False, 'Message': str(e)}), 400