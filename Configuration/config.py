"""
    This file contains configuration of app.
     app db and mail are initialized here.
"""

from flask_mongoengine import MongoEngine
from flask_mail import Mail

db = MongoEngine()
mail = Mail()


def initialize_db(app):
    """
        Initializes the MongoEngine database object
    """
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://manoj:practice@pythoncluster.uf4o4.mongodb.net/calorie_tracker?retryWrites=true&w=majority'
    }
    db.init_app(app)


def initialize_mail(app):
    """
        Initializes the Flask Mail object
    """
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'tester2049tester@gmail.com'
    app.config['MAIL_PASSWORD'] = 'test@2049'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)
