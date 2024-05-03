#!/bin/bash

echo "Installing dependencies..."

python3 -m pip install -r requirements.txt

echo "Migrating database..."

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Creating superuser..."

python3 manage.py createsuperuser --noinput || true

echo "Collecting static files..."

python3 manage.py collectstatic --noinput