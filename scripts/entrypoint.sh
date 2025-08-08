#!/usr/bin/env bash
set -e

# Optional: wait for DB to be reachable
python - <<'PY'
import time, os
import psycopg2
for i in range(30):
    try:
        psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT", "5432"),
        )
        print("DB reachable"); break
    except Exception as e:
        print("Waiting for DB...", e); time.sleep(2)
PY

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn kds_project.wsgi:application --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3}
