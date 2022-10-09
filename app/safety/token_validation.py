import jwt
from functools import wraps
from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
from safety.key import secret_key

def token_required(func):
	# decorator factory which invoks update_wrapper() method and passes decorated function as an argument
	@wraps(func)
	def decorated(*args, **kwargs):
		token = request.form['token']
		if not token:
			return jsonify({'Alert': 'Token is missing!'}), 401
		try:
			data = jwt.decode(token, secret_key, algorithms="HS256")
		# You can use the JWT errors in exception
		# except jwt.InvalidTokenError:
		#	 return 'Invalid token. Please log in again.'
		except:
			return jsonify({'Message': 'Invalid token'}), 403
		return func(*args, **kwargs)
	return decorated
