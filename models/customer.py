from db import db
from .person import PersonModel

class CustomerModel(PersonModel):
    phoneNr = db.Column(db.String(80)) # TODO change datatype
    email = db.Column(db.String(80))

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
    
