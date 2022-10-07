from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'

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
