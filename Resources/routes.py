from controllers.controller import UserApi, UsersApi


def initialize_routes(api):
    api.add_resource(UserApi, '/users/<email>')
    api.add_resource(UsersApi, '/users')
