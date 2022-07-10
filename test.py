# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_ECHO'] = True
# db = SQLAlchemy(app)

# class BaseModel(db.Model):
#     __abstract__ = True
#     id = db.Column(db.Integer, primary_key=True)

# class A(BaseModel):
#     a_name = db.Column(db.String)
#     a_type = db.Column(db.String)
#     __mapper_args__ = {
#         'polymorphic_on': a_type,
#         'polymorphic_identity': 'a',
#     }

# class B(BaseModel):
#     b_name = db.Column(db.String)
#     b_type = db.Column(db.String)
#     __mapper_args__ = {
#         'polymorphic_identity': 'b',
#         'polymorphic_on': b_type
#     }

# class Inheritance(A, B):
#     a_id = db.Column(db.ForeignKey(A.id), primary_key=True)
#     b_id = db.Column(db.ForeignKey(B.id), primary_key=True)
#     name = db.Column(db.String)

# db.create_all()
# db.session.add_all((A(), B()))
# db.session.commit()
# db.session.add(Inheritance(a_id=1, b_id=1))
# db.session.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship("Pet", backref="owner", lazy="dynamic")

    
class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship(db.Integer, db.ForeignKey("person.id"))