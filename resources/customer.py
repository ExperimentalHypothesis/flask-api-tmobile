from flask_restful import Resource, reqparse
from models.customer import CustomerModel 

class Customer(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("firstName", type=str, required=True, help="first name of customer")
    parser.add_argument("lastName", type=str, required=True, help="last name of customer")
    parser.add_argument("dob", type=str, required=True, help="date of birth of customer")
    parser.add_argument("phoneNr", type=str, required=True, help="phone nr of customer")
    parser.add_argument("email", type=str, required=True, help="email of customer")

    def get(self, id):
        customer = CustomerModel.findById(id)
        if customer:
            return customer.json(), 200
        return {"msg": f"customer with id {id} not found"}, 404

    def post(self): ## todo check email is unique
        payload = self.parser.parse_args()
        customer = CustomerModel(**payload)
        customer.saveToDB()
        return {"msg": "customer created successfully."}, 201
 
    def delete(self, id): ## todo based on email as it is unique
        customer = CustomerModel.findById(id)
        if customer:
            customer.deleteFromDB()
            return {"msg": "customer deleted succesfully."}, 204
        return {"msg": f"customer with id {id} not found"}, 404

    def put(self, id):
        payload = self.parser.parse_args()
        customer = CustomerModel.findById(id)
        if customer:
            customer.firstName = payload["firstName"]
            customer.lastName = payload["lastName"]
            customer.dob = payload["dob"]
            customer.phoneNr = payload["phoneNr"]
            customer.email = payload["email"]
        else:
            customer = CustomerModel(**payload)
        customer.saveToDB()
        return customer.json(), 201


            


        

    

     
    