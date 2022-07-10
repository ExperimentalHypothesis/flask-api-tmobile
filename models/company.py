from db import db

class CompanyModel(db.Model):

    __tablename__  = "companies"

    id = db.Column(db.Integer, primary_key=True)
    ico = db.Column(db.Integer)
    dic = db.Column(db.Integer)
    company_type = db.Column(db.String(20))

    __mapper_args__ = {
        "polymorphic_identity": "company",
        "polymorphic_on": "company_type",

    }

    def __init__(self, ico, dic):
        self.ico = ico
        self.dic = dic

    def __repr__(self):
        return f"<CompanyModel {self.ico}>"

    def json(self):
        return {"ico": self.ico, "dic": self.dic}
    
    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

