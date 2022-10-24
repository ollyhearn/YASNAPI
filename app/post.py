from flask import Blueprint, request, jsonify, session, make_response
from db.models import db, PostModel
from safety.token_validation import token_required
from safety.key import secret_key
import jwt
from datetime import datetime, timedelta

post_b = Blueprint("post", __name__)

@post_b.route("/", methods=["GET"])
def index():
	postid = request.args.get("postid", default=None, type=int)
	if postid:
		post = PostModel.query.filter_by(id=postid).first()
		if post:
			return jsonify(post.as_dict()), 200
		else:
			return jsonify({'Message': 'Post not found'}), 403
	return "OK", 200

@post_b.route("/fetch", methods=["GET"])
def fetchten():
	posts = PostModel.query.all()
	response = {}
	for post in posts:
		response[post.as_dict()['id']] = post.as_dict()
	return response

@token_required
@post_b.route("/newpost", methods=["POST"])
def newpost():
	text = request.form.get('text', None)
	title = request.form.get('title', None)
	if not text:
		return jsonify({'Message': 'Provide text at least'}), 403
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	new_post = PostModel(text=text, owner=data['id'], title=title)
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'Message': 'Post created'}), 200
