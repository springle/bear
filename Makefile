get-classes:
	docker-compose exec backend python3 manage.py getclasses

shell:
	docker-compose exec backend bash

migrate:
	docker-compose exec backend python3 manage.py makemigrations
	docker-compose exec backend python3 manage.py migrate

superuser:
	docker-compose exec backend python3 manage.py createsuperuser

psql:
	docker-compose exec db psql -U postgres
