# Recipe App API
To start the Django App, first clone the repo:

## Getting started
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

#### (Step-by-step)


## Postgres 
sudo -u postgres psql
alter user postgres with encrypted password 'secretpassword';

OPEN A EXTERNAL TERMINAL : 

sudo -u postgres psql
OR 
psql -U postgres
in your terminal to get into postgres

CREATE USER new_username;
ALTER USER new_username SUPERUSER CREATEDB;


## REST API using DJANGO REST

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py runserver


```