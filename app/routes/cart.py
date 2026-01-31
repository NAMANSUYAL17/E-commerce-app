from flask import Blueprint,redirect,url_for,render_template
from flask_login import login_required,current_user
from app import db
from app.models import Cart
cart=Blueprint('cart',__name__)
@cart.route("/add-to-cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    item = Cart.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first()

    if item:
        item.quantity += 1
    else:
        item = Cart(
            user_id=current_user.id,
            product_id=product_id
        )
        db.session.add(item)

        db.session.commit()
    return redirect(url_for('shop.products'))
@cart.route("/cart")
@login_required
def view_cart():
    cart_items=Cart.query.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", cart_items=cart_items)
