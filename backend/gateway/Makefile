format:
	docker-compose exec gateway bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build gateway

up-dev:
	docker-compose start gateway

bash:
	docker-compose exec gateway bash

test:
	docker-compose exec gateway bash  -c "TEST_MODE=true coverage run --source=src -m pytest -s $(location)"

coverage-html:
	docker-compose exec gateway bash -c "coverage html"

