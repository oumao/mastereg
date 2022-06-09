from flask_restful import Resource


class StudentList(Resource):

    def post(self):
        pass

    def get(self):
        pass

class Student(Resource):

    def get(self, uuid):
        pass

    def put(self, uuid):
        pass

    def delete(self, uuid):
        pass