FROM python:3.7

WORKDIR /csapi
ENV PYTHONUNBUFFERED 0

RUN apt update -y
RUN apt install -y wget
COPY download_model.sh /csapi
COPY requirements.txt requirements.txt
RUN sh download_model.sh
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential libgl1-mesa-dev
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb

CMD python manage.py runserver 0.0.0.0:8000
