#!/usr/bin/env bash
python3 manage.py collectstatic
python3 manage.py loaddata db.json
python3 manage.py runserver 0:8000
