from flask_restful import Resource, reqparse
from models.person import PersonModel 


class Person(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("firstName", type=str, required=True, help="first name of person")
    parser.add_argument("lastName", type=str, required=True, help="last name of person")
    parser.add_argument("dob", type=str, required=True, help="date of birth of person")

    def get(self, id):
        person = PersonModel.findById(id)
        if person:
            return person.json(), 200
        return {"msg": f"person with id {id} not found"}, 404

    def post(self):
        payload = self.parser.parse_args()
        person = PersonModel(**payload)
        person.saveToDB()
        return {"msg": "person created successfully."}, 201
     
    def delete(self, id):
        person = PersonModel.findById(id)
        if person:
            person.deleteFromDB()
            return {"msg": "person deleted succesfully."}, 204
        return {"msg": f"person with id {id} not found"}, 404

    def put(self, id):
        payload = self.parser.parse_args()
        person = PersonModel.findById(id)
        if person:
            person.firstName = payload["firstName"]
            person.lastName = payload["lastName"]
            person.dob = payload["dob"]
        else:
            person = PersonModel(**payload)
        person.saveToDB()
        return person.json(), 201
