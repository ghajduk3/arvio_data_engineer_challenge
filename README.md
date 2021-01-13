# ARVIO DATA ENGINEER CHALLENGE
##### author: Gojko Hajdukovic, 01.2021

Table of contents:
1. [Setup](#setup)

<a name="setup"></a>
### Setup
1. In order to install all the project related dependencies issue :
```shell script

cd <repo_root>
pip install -r requirements.txt  
```

2. Postgres database is localhosted and run as docker container. In order to setup database run:

```shell script
docker run -d --name db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=arvio_database -p 5432:5432 postgres:13
```
After the docker container is running rename the .env_example to .env and change the database settings as created in the previous step.

3. After the db is setted up, database is migrated.

```shell script
cd <repo_root>
python manage.py makemigrations arvio_challenge
python manage.py migrate arvio_challenge
```
4.Run django server
```shell script
python manage.py runserver
```
5. After the application is started make a get request to http://localhost:8000/arvio/fill-db in order to fill the db with sample data.
   After the successfull setup you can explore and search the certificates db on http://localhost:8000/arvio/.
   Sample property id that can be searched is `1772-1744-2`.








