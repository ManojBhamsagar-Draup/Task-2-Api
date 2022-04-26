from Models.model import Users, Admin
from flask import Response, request
import json
from flask_restful import Resource
from Models.UserErrors import *


class UserApi(Resource):
    def get(self, email):
        try:
            user = Users.objects.get(email=email).to_json()
            if user == "":
                raise UserNotFoundError("The user doesn't exists")
            return Response(user, mimetype='application/json', status=200)
        except UserNotFoundError:
            res = email + "does not exists"
            return Response(res, mimetype='application/json', status=404)


class UsersApi(Resource):
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


