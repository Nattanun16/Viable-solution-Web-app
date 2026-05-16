#!/bin/bash

# Navigate to the Django project directory
cd viable_graph_project

# Wait for database
while ! nc -z dbs 5432; do
  sleep 0.1
done

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start server
python manage.py runserver 0.0.0.0:8000
