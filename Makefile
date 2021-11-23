postgres-user = postgres
postgres-database = postgres
tortoise-config = src.settings.TORTOISE_CONFIG

format:
	docker-compose exec backend bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build

up-dev:
	docker-compose run --rm backend bash -c "aerich init-db && aerich upgrade"
	docker-compose up

backend-bash:
	docker-compose exec backend bash

frontend-bash:
	docker-compose exec frontend bash

db-bash:
	docker-compose exec db bash

db-shell:
	docker-compose exec db psql -U $(postgres-user)

recreate-db:
	docker-compose stop backend
	docker-compose exec db bash -c "runuser postgres -c 'dropdb $(postgres-database); createdb $(postgres-database)'"
	docker-compose exec db psql -U postgres -a -f /docker-entrypoint-initdb.d/init-postgres.sql
	docker-compose start backend

aerich-init:
	docker-compose exec backend bash -c "aerich init --tortoise-orm $(tortoise-config)"

aerich-init-db:
	docker-compose exec backend bash -c "aerich init-db"

aerich-migrate:
	docker-compose exec backend bash -c "aerich migrate"

aerich-upgrade:
	docker-compose exec backend bash -c "aerich upgrade"

migrations:
	make aerich-migrate && make aerich-upgrade

test:
	docker-compose exec backend bash  -c "TEST_MODE=true coverage run --source=src -m pytest -s $(location)"

coverage-html:
	docker-compose exec backend bash -c "coverage html"

