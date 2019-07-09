
FROM alpine

# Project Files and Settings

RUN mkdir /Django

ADD . /Django/


WORKDIR /Django


RUN apk update
RUN apk upgrade
RUN apk --no-cache add \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext \ 
    unzip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r requirements.txt

RUN unzip -o urteile.zip

