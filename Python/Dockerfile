FROM python:3.11.0-alpine3.16

WORKDIR /home/python

COPY . .

RUN apk update
RUN apk add build-base 
RUN apk add libpq-dev 
RUN pip install psycopg2