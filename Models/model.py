from mongoengine import *
from Configuration.config import db
from uuid import uuid4
from flask_bcrypt import generate_password_hash, check_password_hash


class Users(db.Document,DynamicDocument):
    name= db.StringField(required=True),
    email= db.StringField(required=True, primary_key=True),
    password= db.StringField(required=True)
    height= db.FloatField(required=True),
    weight= db.FloatField(required=True),
    age= db.IntField(required=True),
    gender= db.StringField(required=True),
    bmi= db.FloatField(),
    calories= db.ListField(default=[]),
    role = db.StringField(required=True, default='user')

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self.bmi = round((self.weight/(self.height ** 2)), 2)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Admin(db.Document):
    email: db.StringField(required=True, primary_key=True)
    password: db.StringField(required=True)
    role: db.StringField(required=True, default="admin")