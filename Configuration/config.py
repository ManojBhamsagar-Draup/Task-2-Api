from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    """
        Initializes the MongoEngine database object
    """
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://manoj:practice@pythoncluster.uf4o4.mongodb.net/calorie_tracker?retryWrites=true&w=majority'
    }
    db.init_app(app)