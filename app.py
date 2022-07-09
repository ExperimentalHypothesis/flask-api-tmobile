from flask import Flask
from flask_restful import Resource, Api
import os

from resources.person import Person

app = Flask(__name__)
app.secret_key = "sadaddaf"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

api = Api(app)
# api.add_resource(Person, "/person/<string:firstName>")
api.add_resource(Person, "/person", "/person/<int:id>", endpoint="person")

# api.add_resource(Company, "/company")
# api.add_resource(Customer, "/customer")
# api.add_resource(Address, "/address")
# api.add_resource(Order, "/order")
# api.add_resource(Item, "/item")


# when developing..
if __name__ == "__main__":

    # this will create tables in db before first request
    @app.before_first_request
    def create_tables():
        db.create_all()

    from db import db
    db.init_app(app)
    app.run(debug=True)







