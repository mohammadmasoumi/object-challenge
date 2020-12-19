FROM python:3.8

COPY / /object_challenge

WORKDIR object_challenge

RUN apt-get -y install libsnappy-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pip --upgrade pip
    && pip install -r requirements/production.txt