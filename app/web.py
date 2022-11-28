from flask import render_template, Blueprint, request, make_response

web_b = Blueprint("web", __name__)

@web_b.route("/")
def index():
	c = request.cookies.get('token', None)
	return render_template("index.html", c=c)

@web_b.route("/posts")
def posts():
	return render_template("posts.html")

@web_b.route("/login")
def login():
	return render_template("login.html")

@web_b.route("/register")
def register():
	return render_template("register.html")
