from controllers.controller import UserApi, UsersApi, UserDataApi
from Resources.auth import LoginApi, SignupApi


def initialize_routes(api):
    """
        Initializing all api end points of the application
    """
    api.add_resource(UserApi, '/users/<email>')
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserDataApi, '/data')
    api.add_resource(SignupApi, '/auth/signup')
    api.add_resource(LoginApi, '/auth/login')
