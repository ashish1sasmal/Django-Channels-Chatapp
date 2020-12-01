web: daphne djangoChat.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=djangoChat.settings -v2