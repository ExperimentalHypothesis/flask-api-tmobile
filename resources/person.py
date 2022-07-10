from flask_restful import Resource, reqparse
from models.person import PersonModel 


class Person(Resource):
    """ Base resource for Customer. """

    parser = reqparse.RequestParser()
    parser.add_argument("firstName", type=str, required=True, help="first name of person")
    parser.add_argument("lastName", type=str, required=True, help="last name of person")
    parser.add_argument("dob", type=str, required=True, help="date of birth of person")

    def get(self, id):
        found = PersonModel.findById(id)
        if found:
            return found.json(), 200
        return {"msg": f"person with id {id} not found"}, 404

    def post(self):
        payload = self.parser.parse_args()
        person = PersonModel(**payload)
        person.saveToDB()
        return {"msg": "person created successfully."}, 201
     
    def delete(self, id):
        found = PersonModel.findById(id)
        if found:
            found.deleteFromDB()
            return {"msg": "person deleted succesfully."}, 204
        return {"msg": f"person with id {id} not found"}, 404

    def put(self):
        pass
