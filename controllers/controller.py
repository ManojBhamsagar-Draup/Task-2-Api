from Models.model import Users
from flask import Response, request
from flask_jwt_extended import jwt_required
from controllers.role_decorator import roles_required
from flask_restful import Resource
from flask_mail import Message
from flask import current_app
from Configuration.config import mail
from Models.UserErrors import *
import matplotlib.pyplot as plt
import ast


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
    @roles_required(['user'])
    def get(self, email):
        user = Users.objects(email=email).to_json()
        data = ast.literal_eval(user[1:-1])
        y = data['calories']
        x = list(range(1, len(y)+1))
        plt.xlabel('days')
        plt.ylabel('calories consumed')
        plt.title(data['name'])
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
                 markersize=12)
        plt.savefig('graph.png')
        email = 'tester2049tester@gmail.com'
        msg = Message('order details', sender=current_app.config.get('MAIL_USERNAME'), recipients=[email])
        msg.body = 'testing'
        with current_app.open_resource("C:\\Users\\manoj\\Desktop\\Task-2-Api") as fp:
            msg.attach("graph.png", "image/png", fp.read())
        mail.send(msg)
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
