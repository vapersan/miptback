FROM python:3.8

MAINTAINER reOiL

WORKDIR /app
COPY web/requirements.txt /app
RUN pip install -r requirements.txt
COPY web/ /app
RUN python3 manage.py migrate  

EXPOSE 8000

ENTRYPOINT ["/app/entry.sh"]
