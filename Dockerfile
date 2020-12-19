FROM python:3.8

LABEL MAINTAINER="Mohammad Masoumi mohammad.masoomy74@gmail.com"

ENV GROUP_ID=1000 \
    USER_ID=1000

COPY / /object_challenge

WORKDIR object_challenge

RUN apt-get -y install libsnappy-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pip --upgrade pip \
    && pip install -r requirements/production.txt

RUN addgroup -g $GROUP_ID object_challenge
RUN adduser -D -u $USER_ID -G object_challenge object_challenge -s /bin/sh

USER object_challenge

EXPOSE 5000
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]


