from controllers.controller import UserApi, UsersApi, UserDataApi
from Resources.auth import LoginApi, SignupApi


def initialize_routes(api):
    api.add_resource(UserApi, '/users/<email>')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserDataApi, '/data/<email>')
    api.add_resource(SignupApi, '/auth/signup')
    api.add_resource(LoginApi, '/auth/login')
