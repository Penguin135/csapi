FROM python:3.7-slim

WORKDIR /csapi
ENV PYTHONUNBUFFERED 0

RUN apt update -y
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install django mysqlclient pillow

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb

CMD python manage.py runserver 0.0.0.0:8000
