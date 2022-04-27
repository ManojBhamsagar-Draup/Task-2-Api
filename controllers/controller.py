from Models.model import Users
from flask import Response, request
from flask_jwt_extended import jwt_required
from controllers.role_decorator import roles_required
from flask_restful import Resource
from Models.UserErrors import *


class UserApi(Resource):
    @jwt_required()
    @roles_required(['admin'])
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
    @jwt_required()
    @roles_required(['admin'])
    def get(self):
        users = Users.objects.to_json()
        return Response(users, mimetype='application/json', status=200)

    @jwt_required()
    @roles_required(['admin'])
    def delete(self):
        body = request.get_json()
        try:
            user = Users.objects(email=body['email']).to_json()
            if user == "[]":
                raise UserNotFoundError("the user doesn't exist")
            Users.objects(email=body['email']).delete()
            return Response('user deleted', mimetype='application/json', status=200)
        except UserNotFoundError:
            res = body['email'] + " does not exist"
            return Response(res, mimetype='application/json', status=404)


class UserDataApi(Resource):
    @jwt_required()
    @roles_required(['admin'])
    def get(self, email):
        user = Users.objects(email=email).to_json()
        print(user)
        return Response(user, mimetype='application/json', status=200)

    @jwt_required()
    def put(self, email):
        user = Users.objects(email=email).to_json()
        if user == "[]":
            res = email + " does not exists"
            return Response(res, mimetype='application/json', status=404)

        body = request.get_json()
        total_calories = body['morning'] + body['afternoon'] + body['night'] + body['extra']
        print(total_calories)
        Users.objects(email=email).update(__raw__={'$push': {'calories': total_calories}})
        return Response("data added", mimetype='application/json', status=200)
