from flask import Blueprint, request, jsonify, session, make_response
from db.models import db, PostModel
from safety.token_validation import token_required
from safety.key import secret_key
import jwt
from datetime import datetime, timedelta

post_b = Blueprint("post", __name__)

@post_b.route("/", methods=["GET"])
def getposts():
	posts = PostModel.query.all()
	response = {}
	for post in posts:
		response[post.as_dict()['id']] = post.as_dict()
	return response

@post_b.route("/<postid>", methods=["GET"])
def getpost(postid):
	if postid:
		post = PostModel.query.filter_by(id=postid).first()
		if post:
			return jsonify(post.as_dict()), 200
		else:
			return jsonify({'Message': 'Post not found'}), 403
	return "OK", 200

@token_required
@post_b.route("/", methods=["POST"])
def newpost():
	data = request.get_json()
	if 'text' in data.keys():
		text = data['text']
	else:
		return jsonify({'Message': 'Text not provided'}), 403
	if 'title' in data.keys():
		title = data['title']
	else:
		title = None
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	new_post = PostModel(text=text, owner=data['id'], title=title)
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'Message': 'Post created'}), 200

@token_required
@post_b.route("/<postid>", methods=["PATCH"])
def editpost(postid):
	postid = int(postid)
	data = request.get_json()
	if 'text' in data.keys():
		text = data['text']
	else:
		return jsonify({'Message': 'Text not provided'}), 403
	if 'title' in data.keys():
		title = data['title']
	else:
		title = None
	token_data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	if text:
		post = PostModel.query.filter_by(id=postid).first()
		if token_data['id'] == int(post.owner):
			post.text = text
			if title:
				post.title = title
			else:
				post.title = text.split(".")[0]
			db.session.commit()
			return jsonify({'Message': 'Post updated'}), 200
		else:
			return jsonify({'Message': 'You are not the post owner'}), 403
	else:
		return jsonify({'Message': 'Not enough data provided'}), 403

@token_required
@post_b.route("/<postid>", methods=["DELETE"])
def deletepost(postid):
	data = jwt.decode(request.headers.get('token'), secret_key, algorithms="HS256")
	if postid:
		post = PostModel.query.filter_by(id=postid).first()
		if data['id'] == post.owner:
			db.session.delete(post)
			db.session.commit()
			return jsonify({'Message': 'Post deleted'}), 200
		else:
			return jsonify({'Message': 'You are not the post owner'}), 403
	else:
		return jsonify({'Message': 'Not enough data provided'}), 403
