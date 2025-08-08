# 1. Build stage
FROM python:3.11-slim AS builder

# Install dependencies
WORKDIR /app
COPY requirements/*.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r base.txt -r prod.txt

# 2. Runtime stage
FROM python:3.11-slim

WORKDIR /app
# System deps for Postgres & collectstatic
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy code & dependencies
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . /app

# Collect static files
ENV DJANGO_SETTINGS_MODULE=kds_project.settings.prod
RUN python manage.py collectstatic --noinput

# Expose port & run
EXPOSE 8000
CMD ["gunicorn", "kds_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
