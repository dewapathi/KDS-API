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

#Docker
docker images
docker ps
docker ps -a
docker logs <container_id>
python manage.py migrate
python manage.py createsuperuser

docker-compose down -v
docker-compose up --build
docker-compose exec web python manage.py migrate

#ecr updating

