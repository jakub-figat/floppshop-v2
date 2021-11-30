build-dev:
	-cp -n ./backend/gateway/config/.env.template ./backend/gateway/config/.env
	-cp -n ./backend/users/config/.env.template ./backend/users/config/.env
	-cp -n .backend/products/config/.env.template ./backend/products/config/.env
	-cp -n ./backend/config/.env.template ./backend/config/.env
	docker-compose build


up-dev:
	docker-compose run --rm users bash -c "aerich init-db; aerich upgrade"
	docker-compose run --rm products bash -c "aerich init-db; aerich upgrade"
	docker-compose run --rm orders bash -c "aerich init-db; aerich upgrade"
	docker-compose up


format:
	docker-compose exec gateway bash -c "isort . && black ."
	docker-compose exec users bash -c "isort . && black ."
	docker-compose exec products bash -c "isort . && black ."
