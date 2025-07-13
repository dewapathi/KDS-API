#Django
django-admin startproject kds_project
python manage.py startapp myapp

django-admin --version

pip install -r requirements/dev.txt

#Create database
brew install postgresql
brew services start postgresql
pg_isready

CREATE DATABASE kds_db;
CREATE USER kds WITH PASSWORD 'kds';
GRANT ALL PRIVILEGES ON DATABASE kds_db TO kds;

psql -h localhost -U myuser -d mydb

python manage.py migrate

dropdb
createdb

#Celery

