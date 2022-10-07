FROM python:latest
LABEL author "OllyHearn <longcat512@gmail.com>"
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_ENV="docker"
CMD gunicorn --bind 0.0.0.0:5000 app:app
