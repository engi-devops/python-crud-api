from app import db
from app.models import tbl_user

def register_user(data):
    new_item = tbl_user(
        name=data['name'],
        phone_number=data['phone_number'],
        description=data.get('description', ''),
        username=data.get('username', '')
    )
    db.session.add(new_item)
    db.session.commit()
    return {'message': 'Item created successfully'}

def register_all_user():
    items = tbl_user.query.all()
    return [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]

def get_register_user(item_id):
    item = tbl_user.query.get(item_id)
    if item:
        return {'id': item.id, 'name': item.name, 'description': item.description}
    return {'message': 'Item not found'}, 404

def update_register_user(item_id, data):
    item = tbl_user.query.get(item_id)
    if item:
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        db.session.commit()
        return {'message': 'Item updated successfully'}
    return {'message': 'Item not found'}, 404

def delete_register_user(item_id):
    item = tbl_user.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {'message': 'Item deleted successfully'}
    return {'message': 'Item not found'}, 404