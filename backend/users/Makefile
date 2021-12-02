postgres-user = postgres
postgres-database = postgres
tortoise-config = src.settings.TORTOISE_CONFIG

format:
	docker-compose exec users bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build users

up-dev:
	docker-compose run --rm users bash -c "aerich init-db; aerich upgrade"
	docker-compose start users

bash:
	docker-compose exec users bash

db-bash:
	docker-compose exec users_db bash

db-shell:
	docker-compose exec users_db psql -U $(postgres-user)

recreate-db:
	docker-compose stop users
	docker-compose exec users_db bash -c "runuser postgres -c 'dropdb $(postgres-database); createdb $(postgres-database)'"
	docker-compose exec users_db psql -U postgres -a -f /docker-entrypoint-initdb.d/init-postgres.sql
	docker-compose start users

aerich-init:
	docker-compose exec users bash -c "aerich init --tortoise-orm $(tortoise-config)"

aerich-init-db:
	docker-compose exec users bash -c "aerich init-db"

aerich-migrate:
	docker-compose exec users bash -c "aerich migrate"

aerich-upgrade:
	docker-compose exec users bash -c "aerich upgrade"

aerich-migrations:
	docker-compose exec users bash -c "aerich migrate"
	docker-compose exec users bash -c "aerich upgrade"

test:
	docker-compose exec users bash -c "TEST_MODE=true coverage run --source=src -m pytest -s $(location)"

coverage-html:
	docker-compose exec users bash -c "coverage html"

