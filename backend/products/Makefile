postgres-user = postgres
postgres-database = postgres
tortoise-config = src.settings.TORTOISE_CONFIG

format:
	docker-compose exec products bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build products

up-dev:
	docker-compose run --rm products bash -c "aerich init-db; aerich upgrade"
	docker-compose up

bash:
	docker-compose exec products bash

db-bash:
	docker-compose exec products_db bash

db-shell:
	docker-compose exec products_db psql -U $(postgres-user)

recreate-db:
	docker-compose stop products
	docker-compose exec products_db bash -c "runuser postgres -c 'dropdb $(postgres-database); createdb $(postgres-database)'"
	docker-compose exec products_db psql -U postgres -a -f /docker-entrypoint-initdb.d/init-postgres.sql
	docker-compose start products

aerich-init:
	docker-compose exec products bash -c "aerich init --tortoise-orm $(tortoise-config)"

aerich-init-db:
	docker-compose exec products bash -c "aerich init-db"

aerich-migrate:
	docker-compose exec products bash -c "aerich migrate"

aerich-upgrade:
	docker-compose exec products bash -c "aerich upgrade"

aerich-migrations:
	docker-compose exec products bash -c "aerich migrate"
	docker-compose exec products bash -c "aerich upgrade"

test:
	docker-compose exec products bash  -c "TEST_MODE=true coverage run --source=src -m pytest -s $(location)"

coverage-html:
	docker-compose exec products bash -c "coverage html"

