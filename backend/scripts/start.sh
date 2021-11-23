#!/usr/bin/env sh

postgres_ready () {
  nc -z -i 2 db 5432
}

until postgres_ready; do
  echo 'PostgreSQL is unavailable, waiting...'
done

echo 'PostgreSQL connection established, continuing...'

exec "$@"