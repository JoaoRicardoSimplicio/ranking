FROM python:3.7

ENV PYTHONDONTWRITTEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN pip install -r requeriments.txt



