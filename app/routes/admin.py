import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, redirect, url_for,current_app
from flask_login import login_required
from app import db
from app.models import Product
from app.forms import AddProductForm

admin=Blueprint('admin',__name__)
def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext =os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(current_app.root_path,'static/uploads',picture_fn)
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
@admin.route("/admin/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    form = AddProductForm()

    if form.validate_on_submit():
        image_file = None
        if form.image.data:
            image_file = save_picture(form.image.data)

        product = Product(
            name=form.name.data,
            price=form.price.data,
            description=form.description.data,
            image=image_file
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for('shop.home'))

    return render_template("add_product.html", form=form)

