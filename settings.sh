#!/bin/sh
. venv/bin/activate
export DATABASE_URL="sqlite:///posts.db"
export APP_SETTINGS="config.DevelopmentConfig"
