from flask import Blueprint, request, jsonify, session
from db.models import db, UserModel
from safety.token_validation import token_required
from safety.key import secret_key
import jwt
from datetime import datetime, timedelta

auth_b = Blueprint("auth", __name__)

@auth_b.route("/", methods=["GET", "POST"])
def root():
	return "OK", 200

@auth_b.route("/login", methods=["POST"])
def login():
	if request.form['username'] and request.form['password']:
		session['logged_in'] = True
		token = jwt.encode({
			'username': request.form['username'],
			'expiration': str(datetime.utcnow() + timedelta(seconds=3600))
		}, secret_key)
		return jsonify({'token': token}) # jwt.decode(token, key=secret_key, algorithms="HS256")
	else:
		return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})

@auth_b.route("/register", methods=["POST"])
def register():
	username = request.form['username']
	password = request.form['password']
	new_user = UserModel(username, password)
	db.session.add(new_user)
	db.session.commit()
	return "User registered", 200

@auth_b.route("/check", methods=["POST"])
@token_required
def check():
	return "You are in!", 200
