#!/bin/bash

echo "Hello, Creating a superuser account for you"
python manage.py createsuperuser --username=${DJANGO_SUPERUSER_USERNAME} --email=${DJANGO_SUPERUSER_EMAIL} --noinput