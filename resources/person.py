from flask_restful import Resource, reqparse
from models.person import PersonModel 

persons = [{"firstName": "lukas", "lastName": "kot", "age": 23}]

class Person(Resource):
    """ Resource for Person. """

    parser = reqparse.RequestParser()
    parser.add_argument("firstName", type=str, required=True, help="first name of person")
    parser.add_argument("lastName", type=str, required=True, help="last name of person")
    parser.add_argument("dob", type=str, required=True, help="date of birth of person")

    def get(self, id):
        foundPerson = PersonModel.findById(id)
        if foundPerson:
            return foundPerson.json(), 200
        return {"msg": f"person with id {id} not found"}, 404

    def post(self):
        payload = Person.parser.parse_args()
        person = PersonModel(**payload)
        person.saveToDB()
        return {"msg": "Person created successfully."}, 201


        

    def delete(self):
        pass

    def put(self):
        pass
