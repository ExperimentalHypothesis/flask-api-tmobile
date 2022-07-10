from db import db

class OrderModel(db.Model):
    __tablename__  = "orders"

    id = db.Column(db.Integer, primary_key=True)
    costs = db.Column(db.Float(precision=2))
    customerId = db.Column(db.Integer, db.ForeignKey("persons.id"))

    def __init__(self, costs, customerId):
        self.costs = costs
        self.customerId = customerId

    def json(self):
        return {"id": self.id, "costs": self.costs, "customerId": self.customerId}

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()