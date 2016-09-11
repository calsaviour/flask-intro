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
