from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
db=SQLAlchemy()
login_manager=LoginManager()
bcrypt=Bcrypt()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='secret123'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ecommerce.db'
    db.__init__(app)
    login_manager.__init__(app)
    bcrypt.__init__(app)
    login_manager.login_view='auth.login'
    from app.routes.auth import auth
    from app.routes.shop import shop
    from app.routes.cart import cart
    from app.routes.admin import admin
    app.register_blueprint(auth)
    app.register_blueprint(shop)
    app.register_blueprint(cart)
    app.register_blueprint(admin)
    return app



