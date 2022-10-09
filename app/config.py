import os
from safety.key import secret_key

class Configuration(object):
	user = os.getenv('POSTGRES_USER')
	pwd = os.getenv('POSTGRES_PASSWORD')
	dbname = os.getenv('POSTGRES_DB')

	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{pwd}@postgres.dev:5432/{dbname}'
	SECRET_KEY = secret_key
