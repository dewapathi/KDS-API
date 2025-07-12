FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements/prod.txt
RUN chmod +x scripts/entrypoint.sh

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]