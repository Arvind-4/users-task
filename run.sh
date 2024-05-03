#!/bin/bash

echo "Running Django Development Server in PORT ${PORT:-8000}"
python manage.py runserver 0.0.0.0:${PORT:-8000} --force-color