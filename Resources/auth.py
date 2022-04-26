from flask import request
import flask_jwt_extended
from flask_restful import Resource
import datetime
from Models.model import Users
# from flask_bcrypt import check_password_hash, generate_password_hash
import ast


class SignupApi(Resource):
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
    def post(self):
        body = request.get_json()
        user = Users.objects(email=body.get('email'))
        record = ast.literal_eval(user.to_json()[1:-1])
        auth = False
        if record['password'] == body.get('password'):
            auth = True
        # hash_pw = generate_password_hash(record['password'], rounds=10).decode('utf8')
        # print(hash_pw)
        # auth = check_password_hash(hash_pw, body.get('password'))
        if not auth:
            return {'error': 'Email or password invalid'}, 401
        # print('auth success')
        expires = datetime.timedelta(days=1)
        access_token = flask_jwt_extended.create_access_token(identity=record['email'], expires_delta=expires)
        return {'token': access_token}, 200
