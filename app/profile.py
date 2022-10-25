from flask import Blueprint, request, jsonify, session, make_response
from db.models import db, ProfileModel
from safety.token_validation import token_required
from safety.key import secret_key
import jwt
from datetime import datetime, timedelta

profile_b = Blueprint("profile", __name__)

@profile_b.route("/", methods=["GET", "POST"])
def root():
	return "OK", 200

@token_required
@profile_b.route("/myprofile", methods=["GET"])
def myprofile():
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	profile_data = ProfileModel.query.filter_by(username=data['username']).first()
	return jsonify(profile_data.as_dict()), 200

@token_required
@profile_b.route("/updateprofile", methods=["POST"])
def updateprofile():
	age = request.form.get('age', None)
	name = request.form.get('name', None)
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	profile = ProfileModel.query.filter_by(username=data['username']).first()
	if not age and not name:
		return jsonify({'Message': 'No data specified'}), 403
	if age:
		profile.age = age
	if name:
		profile.name = name
	db.session.commit()
	return jsonify({'Message': 'Data updated'}), 403

@token_required
@profile_b.route("/deleteprofile", methods=["DELETE"])
def deleteprofile():
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	profile = ProfileModel.query.filter_by(id=data['id']).first()
	db.session.delete(profile)
	return jsonify({'Message': 'Profile deleted'}), 200
