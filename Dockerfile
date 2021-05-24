# syntax=docker/dockerfile:1

FROM python:3.9.5-alpine3.13

COPY requirements.txt  /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app /app

# EXPOSE 80

CMD uvicorn app.main:app --host 0.0.0.0 --port 80