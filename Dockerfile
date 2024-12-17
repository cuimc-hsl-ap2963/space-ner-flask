# syntax=docker/dockerfile:1

FROM python:3.12

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "flaskapp:app"]