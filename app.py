from flask import Flask
from Configuration.config import initialize_db
from Resources.routes import initialize_routes
from flask_restful import Api


app = Flask(__name__)

api = Api(app)
initialize_db(app)
initialize_routes(api)


if __name__ == "__main__":
    app.run(debug=True)