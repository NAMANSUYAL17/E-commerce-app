from app import db
from flask_login import UserMixin
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(200))
    password=db.Column(db.String(200))
    cart_items = db.relationship('Cart', backref='user', lazy=True)
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    price=db.Column(db.Float)
    image=db.Column(db.String(100))
    description=db.Column(db.Text)
    cart_items = db.relationship('Cart', backref='product', lazy=True)
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # 🔑 Foreign Keys
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        nullable=False
    )

    quantity = db.Column(db.Integer, default=1)

