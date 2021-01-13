Instructions 
1. Run postgres as docker container
     docker run -d --name db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=arvio_database -p 5432:5432 postgres:13

2. Copy .env_example to .env
   
3. Activate venv
    source venv/bin/activate
   
4. Create db migrations
    python manage.py makemigrations
    python manage.py migrate
   
4. Run django server 
    python manage.py runserver

5. Server will start on localhost
    Make a get request to http://127.0.0.1:8000/arvio/fillData in order to fill the db with data
   
6. Property informations can be searched through web form on http://127.0.0.1:8000/arvio/