from flask import Blueprint,render_template,request
from app.models import Product
shop=Blueprint('shop',__name__)
@shop.route("/")
def home():
    return render_template("home.html")
@shop.route("/product")
def products():
    page = request.args.get('page', 1, type=int)  # current page
    per_page = 6  # products per page

    products = Product.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return render_template("products.html", products=products)