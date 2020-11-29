#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

# create superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='$DJANGO_ADMIN_EMAIL', is_superuser=True).delete(); User.objects.create_superuser('$DJANGO_ADMIN_USERNAME', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | python3 manage.py shell

gunicorn -w 4 -b 0.0.0.0:8000 hermes.wsgi --reload
