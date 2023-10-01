FROM python:alpine3.18

RUN mkdir -p /src /log

WORKDIR /src

COPY tools/requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt
