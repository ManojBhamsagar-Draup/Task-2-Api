from flask import Flask
from Configuration.config import initialize_db, initialize_mail
from Resources.routes import initialize_routes
from flask_restful import Api
from flask_jwt_extended import JWTManager


app = Flask(__name__)

api = Api(app)
app.config["JWT_SECRET_KEY"] = "subconcious@mind"
jwt = JWTManager(app)
initialize_db(app)
initialize_mail(app)
initialize_routes(api)


if __name__ == "__main__":
    app.run(debug=True)