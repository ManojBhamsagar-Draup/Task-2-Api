from Models.model import Users, Admin
from flask import Response, request
import json
from flask_restful import Resource


class UserApi(Resource):
    def get(self):
        users = Users.objects.to_json()
        return Response(users, mimetype='application/json', status=200)

    def post(self):
        print(request)
        body = request.get_json()
        print(body)
        print(type(body))
        user = Users(**body).save()
        return {'name': user.name}, 200