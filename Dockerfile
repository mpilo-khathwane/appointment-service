FROM python:3.7

LABEL maintainer="mpilo.khathwane@gmail.com"

ENV SERVICE_TTL 300
ENV TZ=Africa/Johannesburg

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt /usr/local/appointment-service/
WORKDIR /usr/local/appointment-service
RUN pip install -r requirements.txt

COPY  . /usr/local/appointment-service
RUN pip install --no-cache-dir -e .

EXPOSE 8575
CMD uwsgi --ini-paste-logged /usr/local/appointment-service/appointment_service/configuration/development.ini
