# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/everka/everka

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN chmod g+rx,o+rx /
#RUN adduser -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/everka/requirements.txt
RUN pwd
RUN pip install -r ../requirements.txt
# RUN django-admin startproject everka
# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/everka/entrypoint.sh

# copy project
COPY . /usr/src/everka/

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/shop/shop/entrypoint.sh"]

