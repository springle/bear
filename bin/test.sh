#!/bin/bash

until $(bash -c "docker-compose exec backend python3 manage.py shell --command='pass' >/dev/null 2>/dev/null"); do
    printf '[test script] waiting for backend container...\n'
    sleep 5
done

docker-compose exec backend python3 manage.py check
