FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add  --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    libressl-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

RUN mkdir app
WORKDIR app
COPY . /app

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt