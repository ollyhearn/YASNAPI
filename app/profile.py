from flask import Blueprint, request, jsonify, session, make_response
from db.models import db, ProfileModel
from safety.token_validation import token_required
from safety.key import secret_key
import jwt
from datetime import datetime, timedelta

profile_b = Blueprint("profile", __name__)

@token_required
@profile_b.route("/", methods=["GET"])
def myprofile():
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	profile_data = ProfileModel.query.filter_by(username=data['username']).first()
	return jsonify(profile_data.as_dict()), 200

@token_required
@profile_b.route("/", methods=["PATCH"])
def updateprofile():
	json_data = request.get_json()
	try:
		age = json_data['age']
		name = json_data['name']
	except KeyError:
		return jsonify({'Message': 'No data specified'}), 403
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	profile = ProfileModel.query.filter_by(username=data['username']).first()
	profile.age = age
	profile.name = name
	db.session.commit()
	return jsonify({'Message': 'Data updated'}), 403

@token_required
@profile_b.route("/", methods=["DELETE"])
def deleteprofile():
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	profile = ProfileModel.query.filter_by(id=data['id']).first()
	db.session.delete(profile)
	db.session.commit()
	return jsonify({'Message': 'Profile deleted'}), 200
