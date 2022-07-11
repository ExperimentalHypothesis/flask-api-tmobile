from flask import Flask
from flask_restful import Resource, Api
import os

from resources.person import Person
from resources.customer import Customer
from resources.order import Order


app = Flask(__name__)

app.secret_key = "sadaddaf"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

api = Api(app)
api.add_resource(Person, "/person", "/person/<int:id>", endpoint="person")
api.add_resource(Customer, "/customer", "/customer/<int:id>", endpoint="customer")
api.add_resource(Order, "/order", "/order/<int:id>", endpoint="order")

# api.add_resource(Company, "/company", "/company/<int:id>", endpoint="company")
# api.add_resource(Adress, "/adress", "/adress/<int:id>", endpoint="adress")
# api.add_resource(Item, "/item", "/item/<int:id>", endpoint="item")


# when developing.. in prod it will be in run.py
if __name__ == "__main__":

    # this will create tables in db before first request
    @app.before_first_request
    def create_tables():
        db.create_all()

    from db import db
    db.init_app(app)
    app.run(debug=True, host="0.0.0.0")







