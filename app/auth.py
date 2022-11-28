from flask import Blueprint, request, jsonify, session, make_response
from db.models import db, AuthModel, ProfileModel
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
	try:
		json_data = request.get_json()
		username = json_data['username']
		password = json_data['password']
	except:
		return make_response('Not enough data provided', 403, {'WWW-Authenticate': 'Basic realm: "Not enough data"'})
	data = AuthModel.query.filter_by(username=username).first()
	if username and password and data and data.username == username and data.password == password:
		session['logged_in'] = True
		token = jwt.encode({
			'id': data.id,
			'username': data.username,
			'expiration': str(datetime.utcnow() + timedelta(seconds=3600))
		}, secret_key)
		return jsonify({'token': token}) # jwt.decode(token, key=secret_key, algorithms="HS256")
	else:
		return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})

@auth_b.route("/register", methods=["POST"])
def register():
	try:
		json_data = request.get_json()
		username = json_data['username']
		password = json_data['password']
	except:
		return make_response('Not enough data provided', 402, {'WWW-Authenticate': 'Basic realm: "Not enough data"'})
	if AuthModel.query.filter_by(username=username).first() == None:
		new_user = AuthModel(username, password)
		db.session.add(new_user)
		db.session.commit()
		data = AuthModel.query.filter_by(username=username).first()
		new_profile = ProfileModel(data.id, username)
		db.session.add(new_profile)
		db.session.commit()
		session['logged_in'] = True
		token = jwt.encode({
			'id': data.id,
			'username': username,
			'expiration': str(datetime.utcnow() + timedelta(seconds=3600))
		}, secret_key)
		return jsonify({'token': token}), 200
	else:
		return make_response('Username is unavailiable', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})

@auth_b.route("/logoff", methods=["GET"])
def logoff():
	try:
		if session['logged_in']:
			session['logged_in'] = False
			session.set_cookie('sessionID', '', expires=0)
	except:
		pass
	return make_response('Logged off', 200, {'WWW-Authenticate': 'Basic realm: "Logged off"'})

@auth_b.route("/check", methods=["GET"])
@token_required
def check():
	return "You are in!", 200
