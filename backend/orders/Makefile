postgres-user = postgres
postgres-database = postgres
tortoise-config = src.settings.TORTOISE_CONFIG

format:
	docker-compose exec orders bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build orders

up-dev:
	docker-compose run --rm orders bash -c "aerich init-db; aerich upgrade"
	docker-compose up

bash:
	docker-compose exec orders bash

db-bash:
	docker-compose exec orders_db bash

db-shell:
	docker-compose exec orders_db psql -U $(postgres-user)

recreate-db:
	docker-compose stop orders
	docker-compose exec orders_db bash -c "runuser postgres -c 'dropdb $(postgres-database); createdb $(postgres-database)'"
	docker-compose exec orders_db psql -U postgres -a -f /docker-entrypoint-initdb.d/init-postgres.sql
	docker-compose start orders

aerich-init:
	docker-compose exec orders bash -c "aerich init --tortoise-orm $(tortoise-config)"

aerich-init-db:
	docker-compose exec orders bash -c "aerich init-db"

aerich-migrate:
	docker-compose exec orders bash -c "aerich migrate"

aerich-upgrade:
	docker-compose exec orders bash -c "aerich upgrade"

aerich-migrations:
	docker-compose exec orders bash -c "aerich migrate"
	docker-compose exec orders bash -c "aerich upgrade"

test:
	docker-compose exec orders bash  -c "TEST_MODE=true coverage run --source=src -m pytest -s $(location)"

coverage-html:
	docker-compose exec orders bash -c "coverage html"

