FROM python:3.9

MAINTAINER Mehdi Sadour

ENV PYTHONBUFFERED 1
RUN mkdir /fun_and_curious
WORKDIR /fun_and_curious
COPY requirements.txt /fun_and_curious/
RUN pip install -r requirements.txt
COPY . /fun_and_curious/