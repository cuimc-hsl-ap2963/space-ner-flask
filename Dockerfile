# syntax=docker/dockerfile:1

FROM python:3.12
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
