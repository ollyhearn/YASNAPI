FROM python:3.11.0-bullseye
LABEL author "OllyHearn <longcat512@gmail.com>"
RUN pip install flask flask-sqlalchemy gunicorn psycopg2-binary pyjwt
# RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
# ENV FLASK_ENV="docker"
ENV FLASK_ENV="development"
ENV FLASK_APP="app"
# CMD gunicorn --bind 0.0.0.0:5000 app:app
CMD flask run --host=0.0.0.0 --port=5000
