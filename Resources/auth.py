"""
    Login or signup to application will generate a jwt token
"""

from flask import request
import flask_jwt_extended
from flask_restful import Resource
import datetime
from Models.model import Users
import ast
from werkzeug.security import check_password_hash


class SignupApi(Resource):
    """
        Signup to app
    """
    def post(self):
        # print(request)
        body = request.get_json()
        # print(body)
        # print(type(body))
        user = Users(**body).save()
        expires = datetime.timedelta(days=1)
        access_token = flask_jwt_extended.create_access_token(identity=user.email, expires_delta=expires)
        return {'name': user.name, 'token': access_token}, 200


class LoginApi(Resource):
    """
        Login to app
    """
    def post(self):
        body = request.get_json()
        user = Users.objects(email=body.get('email'))
        record = ast.literal_eval(user.to_json()[1:-1])
        auth = False
        if check_password_hash(record['password'], body.get('password')):
            auth = True
        if not auth:
            return {'error': 'Email or password invalid'}, 401
        # print('auth success')
        expires = datetime.timedelta(days=1)
        access_token = flask_jwt_extended.create_access_token(identity=record['email'], expires_delta=expires)
        return {'token': access_token}, 200
