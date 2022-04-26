from controllers.controller import UserApi, UsersApi
from Resources.auth import LoginApi


def initialize_routes(api):
    api.add_resource(UserApi, '/users/<email>')
    api.add_resource(UsersApi, '/users')
    api.add_resource(LoginApi, '/auth/login')
