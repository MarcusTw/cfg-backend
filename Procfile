web: gunicorn CFG.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py loaddata education_level.json
release: python manage.py loaddata regions.json
release: python manage.py runserver