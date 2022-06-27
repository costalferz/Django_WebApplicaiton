web: gunicorn elon.wsgi --log-file -
release: python manage.py collectstatic --no-input
         python manage.py migrate