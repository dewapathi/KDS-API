#!/bin/bash

set -e

# Wait for database
if [ "$DB_ENGINE" = "postgresql" ]; then
  until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
  done
fi

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

exec "$@"