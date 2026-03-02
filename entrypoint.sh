#!/bin/sh

# Wait for database (optional but helpful)
echo "Running migrations..."
python manage.py migrate --noinput

# Start the application
echo "Starting server..."
exec gunicorn serolink.asgi:application --bind 0.0.0.0:10000