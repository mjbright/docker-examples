FROM python:2.7

MAINTAINER "Docker Build Lab" <dockerlab@mjbright.net>

WORKDIR /src

ADD requirements.txt /src/

RUN pip install -r requirements.txt

ADD . /src

CMD python flask_redis_app.py

