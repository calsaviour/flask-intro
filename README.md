Steps to create heroku db

Setup env var
0. heroku config:set APP_SETTINGS=config.ProductionConfig --remote heroku

This will create the initial db
1. heroku addons:create heroku-postgresql:hobby-dev

Attach the db to app
Created postgresql-shaped-74192 as DATABASE_URL
2. heroku pg:promote postgresql-shaped-74192

run the deployed app
3. heroku run python app.py   


Check db is created
4. heroku config | grep HEROKU_POSTGRESQL

Deploy db. ensure psycopg2 is installed
5. heroku run python db_create.py



Migrating db
1. install flask migrate
2. create file manage.py, add the necessary configuration
3. run python manage.py db init
4. update the models.py
5. run python manage.py db migrate, to generate schema version
6. run python manage.py db upgrade
