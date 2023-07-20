from flask import Blueprint, render_template, request
from model.product import ProductTable
from model.model import db 
from model.encryption import bcrypt

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/", methods=["POST", "GET"])
def something():
    if request.method  == "POST":
        form = request.form 
        product_name = form["product_name"]
        
        product = ProductTable(name=product_name)
        
        placeholder = bcrypt.generate_password_hash(product_name)
        print(placeholder)

        db.session.add(product)
        db.session.commit()

    return render_template("index.html")