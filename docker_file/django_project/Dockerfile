FROM python:3.7.9-stretch

WORKDIR /mydjango

COPY bookmark ./bookmark
COPY mysite2 ./mysite2
COPY manage.py ./manage.py
COPY db.sqlite3 ./db.sqlite3

RUN apt-get update
RUN apt-get install -y vim
RUN pip install django
RUN pip install mysqlclient

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]