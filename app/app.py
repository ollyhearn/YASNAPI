from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

from auth import auth_b
from db.models import db, UserModel

app = Flask(__name__)
app.config.from_object(config.Configuration)

db.init_app(app)

app.register_blueprint(auth_b, url_prefix="/auth")

@app.route('/', methods=["GET", "POST"])
def root():
	return "Hi there!", 200


if __name__ == 'main':
	app.run(debug=True)
