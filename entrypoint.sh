#!/bin/bash

# Prepare log files and start outputting logs to stdout
export DJANGO_SETTINGS_MODULE=projectx.settings

exec gunicorn projectx.wsgi:application \
    --name projectx_django \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --log-level=info \
"$@"
