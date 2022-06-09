from flask import Flask, jsonify, request
from flask_restful import Api

# local imports
from resources.students import StudentList, Student


app = Flask(__name__)
api = Api(app)




# class TodoList(Resource):

#     def get(self):
#         todo = [todo for todo in todos]
#         return jsonify(todo)

# class Todo(Resource):

#     def get(self, id):
#         pass
            
#     def post(self):
#         pass

#     def patch(self, id):
#         pass

#     def delete(self, id):
#         pass

api.add_resource(StudentList, '/students')
api.add_resource(Student, '/students/<str:id>')

if __name__ == '__main__':
    app.run(debug=True)