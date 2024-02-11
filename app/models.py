from datetime import datetime
from app import db

class tbl_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<tbl_user %r>' % self.name