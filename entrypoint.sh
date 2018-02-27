#!/bin/sh

cd /var/www/ideax

export DJANGO_SETTINGS_MODULE=ideax.settings

if [ ! -f /var/www/ideax/.env ]; then
  echo SECRET_KEY=my_super_secret_key > /var/www/ideax/.env
  if [ ! -d /var/www/ideax/static ]; then
    python manage.py collectstatic
  fi

python manage.py migrate

exec gunicorn ideax.wsgi:application \
    --name ideax_django \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --log-level=info \
"$@"
