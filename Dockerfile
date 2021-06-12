# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/Post
COPY requirements.txt /usr/src/Post/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/Post