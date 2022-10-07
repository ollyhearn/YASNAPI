from flask import Blueprint, request, jsonify
from db.models import db, UserModel

auth_b = Blueprint("auth", __name__)

@auth_b.route("/", methods=["GET", "POST"])
def root():
	return "OK", 200

@auth_b.route("/login", methods=["POST"])
def login():
	username = request.form['username']
	password = request.form['password']
	pass

@auth_b.route("/register", methods=["POST"])
def register():
	username = request.form['username']
	password = request.form['password']
	new_user = UserModel(username, password)
	db.session.add(new_user)
	db.session.commit()
	return "User registered", 200
