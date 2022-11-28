from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

from auth import auth_b
from profile import profile_b
from post import post_b
from web import web_b
from db.models import db, AuthModel



app = Flask(__name__)
app.config.from_object(config.Configuration)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

db.init_app(app)

app.register_blueprint(auth_b, url_prefix="/auth")
app.register_blueprint(profile_b, url_prefix="/profile")
app.register_blueprint(post_b, url_prefix="/post")
app.register_blueprint(web_b, url_prefix="/web")

@app.route('/', methods=["GET", "POST"])
def root():
	return "Hi there!", 200

def get_app():
	return app

if __name__ == 'main':
	app.run(debug=True)
