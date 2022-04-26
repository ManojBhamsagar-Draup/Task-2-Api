from mongoengine import *
from Configuration.config import db
from uuid import uuid4


class Users(db.Document,DynamicDocument):
    _id= db.UUIDField(default=uuid4()),
    name= db.StringField(required=True),
    email= db.StringField(required=True, primary_key=True),
    height= db.FloatField(required=True),
    weight= db.FloatField(required=True),
    age= db.IntField(required=True),
    gender= db.StringField(required=True),
    bmi= db.FloatField(),
    calories= db.ListField()


class Admin(db.Document):
    email: db.StringField(required=True, primary_key=True)
    password: db.StringField(required=True)