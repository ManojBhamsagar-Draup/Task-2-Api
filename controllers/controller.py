from Models.model import Users, Admin
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from Models.UserErrors import *


class UserApi(Resource):
    def get(self, email):
        try:
            user = Users.objects(email=email).to_json()
            print(type(user))
            if user == "[]":
                raise UserNotFoundError("The user doesn't exists")
            return Response(user, mimetype='application/json', status=200)
        except UserNotFoundError:
            res = email + " does not exists"
            return Response(res, mimetype='application/json', status=404)


class UsersApi(Resource):
    def get(self):
        users = Users.objects.to_json()
        return Response(users, mimetype='application/json', status=200)


class UserDataApi(Resource):
    @jwt_required()
    def get(self, email):
        user = Users.objects(email=email).to_json()
        print(user)
        return Response(user, mimetype='application/json', status=200)


