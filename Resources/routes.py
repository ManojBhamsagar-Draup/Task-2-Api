from controllers.controller import UserApi


def initialize_routes(api):
    api.add_resource(UserApi, '/users')