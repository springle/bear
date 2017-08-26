#!/bin/bash
until $(bash -c "</dev/tcp/db/5432 >/dev/null"); do
	printf '.'
	sleep 5
done
bash -c "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"
