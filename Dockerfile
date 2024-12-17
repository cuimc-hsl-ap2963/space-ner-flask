# syntax=docker/dockerfile:1

FROM python:3.12

COPY . .

RUN pip3 install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8080 app:app