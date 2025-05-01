#!/usr/bin/env bash

echo "Aplicando migraciones..."
python manage.py migrate

echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando servidor con Gunicorn..."
gunicorn webcafe.wsgi:application
