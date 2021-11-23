#!/usr/bin/env sh

postgres_ready () {
  nc -z -i 2 "$POSTGRES_HOST" "$POSTGRES_PORT"
}

until postgres_ready; do
  echo 'PostgreSQL is unavailable, waiting...'
done

echo 'PostgreSQL connection established, continuing...'

exec "$@"