from db import db

class PersonModel(db.Model):

    __tablename__  = "persons"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    dob = db.Column(db.String(80)) # TODO change datatype
    person_type = db.Column(db.String(20))

    __mapper_args__ = {
        "polymorphic_on": "person_type",
        "polymorphic_identity": "person",
    }

    def __init__(self, firstName, lastName, dob):
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob

    def __repr__(self):
        return f"<PersonModel {self.firstName}, {self.lastName}>"

    def json(self):
        return {"firstName": self.firstName, "lastName": self.lastName, "dob": self.dob}

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
