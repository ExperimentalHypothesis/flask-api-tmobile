from flask_restful import Resource, reqparse
from models.order import OrderModel 


class Order(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("costs", type=int, required=True, help="costs is needed")
    parser.add_argument("customerId", type=int, required=True, help="every order needs a customerId")

    def get(self, id):
        order = OrderModel.findById(id)
        if order:
            return order.json(), 200
        return {"msg": f"order with id {id} not found"}, 404

    def post(self):
        payload = self.parser.parse_args()
        print(payload)
        order = OrderModel(**payload)
        order.saveToDB()
        return {"msg": "order created successfully."}, 201
     
    def delete(self, id):
        order = OrderModel.findById(id)
        if order:
            order.deleteFromDB()
            return {"msg": "order with id {id} deleted succesfully."}, 204
        return {"msg": f"order with id {id} not found"}, 404

    def put(self, id):
        payload = self.parser.parse_args()
        order = OrderModel.findById(id)
        if order:
            order.costs = payload["costs"]
        else:
            order = OrderModel(**payload)
        order.saveToDB()
        return order.json(), 201
