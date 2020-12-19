FROM python:3.8

LABEL MAINTAINER="Mohammad Masoumi mohammad.masoomy74@gmail.com"

ENV GROUP_ID=1000 \
    USER_ID=1000

COPY / /object_challenge

WORKDIR object_challenge

RUN apt-get update \
    && apt-get -y install libsnappy-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pip --upgrade pip \
    && pip install -r requirements/production.txt

RUN addgroup -g $GROUP_ID flask
RUN adduser -D -u $USER_ID -G flask flask -s /bin/sh

USER flask

EXPOSE 5000
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
