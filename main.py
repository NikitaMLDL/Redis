from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import redis

app = Flask(__name__)
api = Api(app)

# Настройка соединения с Redis
r = redis.Redis(host='localhost', port=6379, db=0)


class UserProfile(Resource):
    def post(self):
        user_id = request.json['user_id']
        if r.exists(user_id):
            return jsonify({"message": "User already exists"})
        r.hmset(user_id, request.json)
        return jsonify({"message": "User created"})

    def put(self, user_id):
        if not r.exists(user_id):
            return jsonify({"message": "User not found"})
        r.hmset(user_id, request.json)
        return jsonify({"message": "User updated"})

    def delete(self, user_id):
        if not r.exists(user_id):
            return jsonify({"message": "User not found"})
        r.delete(user_id)
        return jsonify({"message": "User deleted"})


class AdminActions(Resource):
    def get(self):
        keys = r.keys()
        users = {key: r.hgetall(key) for key in keys}
        return jsonify(users)

    def delete(self):
        r.flushdb()
        return jsonify({"message": "All users deleted"})


api.add_resource(UserProfile, '/user', '/user/<string:user_id>')
api.add_resource(AdminActions, '/admin')

if __name__ == '__main__':
    app.run(debug=True)