FROM python:3.8-slim-buster

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBRFFERED 1

# install system dependencies
RUN apt-get update \
	&& apt-get -y install netcat gcc \
	&& apt-get clean \
	&& apt-get -y install nano


# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY . /backend
