from flask_restful import Resource, reqparse
from models.customer import CustomerModel 

class Customer(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("firstName", type=str, required=True, help="first name of person")
    parser.add_argument("lastName", type=str, required=True, help="last name of person")
    parser.add_argument("dob", type=str, required=True, help="date of birth of person")
    parser.add_argument("phoneNr", type=str, required=True, help="phone nr of person")
    parser.add_argument("email", type=str, required=True, help="email of person")

    def get(self, id):
        found = CustomerModel.findById(id)
        if found:
            return found.json(), 200
        return {"msg": f"customer with id {id} not found"}, 404

    def post(self):
        payload = self.parser.parse_args()
        customer = CustomerModel(**payload)
        customer.saveToDB()
        return {"msg": "customer created successfully."}, 201

    def delete(self, id):
            found = CustomerModel.findById(id)
            if found:
                found.deleteFromDB()
                return {"msg": "customer deleted succesfully."}, 204
            return {"msg": f"customer with id {id} not found"}, 404

    

     
    