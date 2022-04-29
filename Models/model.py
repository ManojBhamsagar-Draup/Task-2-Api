from mongoengine import *
from Configuration.config import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class Users(db.Document, DynamicDocument, UserMixin):
    """
        Schema of Users collection
    """
    name = db.StringField(required=True),
    email = db.StringField(required=True, primary_key=True),
    password = db.StringField(required=True)
    height = db.FloatField(required=True),
    weight = db.FloatField(required=True),
    age = db.IntField(required=True),
    gender = db.StringField(required=True),
    bmi = db.FloatField(),
    calories = db.ListField(default=[]),
    role = db.StringField(required=True, default='user')

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self.bmi = round((self.weight/(self.height ** 2)), 2)
        self.password = generate_password_hash(self.password)
