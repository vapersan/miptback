FROM python:3.8

MAINTAINER reOiL

COPY web/ /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
EXPOSE 8080

CMD python3 /app/manage.py runserver 0:8080
