from flask_restful import Resource, reqparse
from models.company import CompanyModel 


class Company(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("ico", type=int, required=True, help="ico is needed")
    parser.add_argument("dic", type=int, required=True, help="dic is needed")

    def get(self, ico):
        company = CompanyModel.findByICO(ico)
        if company:
            return company.json(), 200
        return {"msg": f"comapny with ICO {ico} not found"}, 404

    def post(self):
        payload = self.parser.parse_args()
        ico = payload["ico"]
        company = CompanyModel.findByIdICO(ico)
        if company:
            return {"msg": f"company with ICO {ico} already exists"}, 400
        company = CompanyModel(**payload)
        company.saveToDB()
        return company.json(), 201

    def delete(self, ico):
        company = CompanyModel.findByICO(ico)
        if company:
            company.deleteFromDB()
            return {"msg": "comapny with ICO {ico} deleted succesfully."}, 204
        return {"msg": f"company with ICO {ico} not found"}, 404

    def put(self, ico):
        payload = self.parser.parse_args()
        company = CompanyModel.findByICO(ico)
        if company:
            company.ico = payload["ico"] 
            company.dic = payload["dic"] 
        else:
            company = CompanyModel(**payload)
        company.saveToDB()
        return company.json(),






