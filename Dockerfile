FROM python:3.8.6

LABEL MAINTAINER="Mohammad Masoumi mohammad.masoomy74@gmail.com"

COPY / /object_challenge

WORKDIR object_challenge

RUN apt-get update \
    && apt-get -y install libsnappy-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pip --upgrade pip \
    && pip install -r requirements/production.txt

EXPOSE 5000
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
