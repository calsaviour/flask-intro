#!/bin/sh
. venv/bin/activate
#export DATABASE_URL="sqlite:///posts.db"
export DATABASE_URL="postgresql://localhost/discover_flask_dev"
export APP_SETTINGS="config.DevelopmentConfig"
