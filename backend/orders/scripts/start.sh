#!/usr/bin/env sh

postgres_ready () {
  nc -z -i 2 "$POSTGRES_HOST" "$POSTGRES_PORT"
}

rabbitmq_ready () {
  nc -z -i 2 "$RABBITMQ_HOST" "$RABBITMQ_PORT"
}

until postgres_ready; do
  echo 'PostgreSQL is unavailable, waiting...'
done

echo 'PostgreSQL connection established, continuing...'

until rabbitmq_ready; do
  echo 'RabbitMQ is unavailable, waiting...'
done

echo 'RabbitMQ connection established, continuing...'

exec "$@"