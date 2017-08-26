#!/bin/bash

until $(bash -c "docker-compose exec backend echo >/dev/null"); do
    printf '.'
    sleep 5
done

docker-compose exec backend python3 manage.py test
