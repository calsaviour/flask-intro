Steps to create heroku db

This will create the initial db
1. heroku addons:create heroku-postgresql:hobby-dev

Attach the db to app
Created postgresql-shaped-74192 as DATABASE_URL
2. heroku pg:promote postgresql-shaped-74192
