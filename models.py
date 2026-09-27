from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    lists = db.relationship('ShoppingList',backref='user',lazy=True)


class ShoppingList(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   items = db.relationship('Item', backref='shopping_list', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    is_bought = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('shopping_list.id'), nullable=False)