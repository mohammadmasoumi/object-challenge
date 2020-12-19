FROM python:3.8.6

LABEL MAINTAINER="Mohammad Masoumi mohammad.masoomy74@gmail.com"

ENV GROUP_ID=2000 \
    USER_ID=2000 \
    USER_NAME=flask

COPY / /object_challenge

WORKDIR object_challenge

RUN apt-get update \
    && apt-get -y install libsnappy-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pip --upgrade pip \
    && pip install -r requirements/production.txt

RUN addgroup -gid $GROUP_ID $USER_NAME
RUN adduser -u $USER_ID -gid $GROUP_ID --disabled-password --gecos '' $USER_NAME

USER $USER_NAME

EXPOSE 5000
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
