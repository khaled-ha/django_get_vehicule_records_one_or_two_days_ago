#!/bin/sh

if [ "$DATABASE" = "db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python shop/manage.py flush --no-input
python shop/manage.py migrate
python shop/manage.py collectstatic --no-input --clear

# exec "$@"
