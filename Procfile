web: gunicorn elon.wsgi --log-file -
release: python manage.py collecstatic --no-input
         python manage.py migrate