from db import db
from .person import PersonModel
# from .company import CompanyModel

class CustomerModel(PersonModel):

    __tablename__  = "customer"

    phoneNr = db.Column(db.Integer)
    email = db.Column(db.String(128))
    customers = db.relationship("OrderModel", backref="ordered_by", lazy="dynamic")

    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }

    def __init__(self, firstName, lastName, dob, phoneNr, email):
        super().__init__(firstName, lastName, dob)
        self.phoneNr = phoneNr
        self.email = email

    def json(self):
        return {"firstName": self.firstName, "lastName": self.lastName, "dob": self.dob, "phoneNr": self.phoneNr, "email":self.email}

    def __repr__(self):
        return f"<CustomerModel {self.email}>"

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()
    
