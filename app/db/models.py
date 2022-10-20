from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class AuthModel(db.Model):
    __tablename__ = 'auth'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    # name = db.Column(db.String())
    # age = db.Column(db.Integer())

    def __init__(self, username, password):
        # self.name = name
        # self.age = age
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.username}"

class ProfileModel(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String())
    name = db.Column(db.String())
    age = db.Column(db.Integer())

    def __init__(self, id, username, age=None, name=None):
        self.id = id
        self.name = name
        self.age = age
        self.username = username

    def __repr__(self):
        return f"{self.username}"

    def as_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class PostModel(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime, default=datetime.now())
    owner = db.Column(db.Integer())
    title = db.Column(db.String())
    text = db.Column(db.String())

    def __init__(self, text, owner, title=None):
        self.owner = owner
        self.text = text
        if not title:
            self.title = self.text.split(".")[0]

    def __repr__(self):
        return f"{self.username}"

    def as_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d
