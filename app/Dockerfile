FROM python:3.11.0-bullseye
LABEL author "OllyHearn <longcat512@gmail.com>"
RUN pip install flask flask-sqlalchemy gunicorn psycopg2-binary pyjwt
# RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
ENV FLASK_ENV="docker"
CMD gunicorn --bind 0.0.0.0:5000 app:app
