# Floppshop V2
Project for micorservices learning puproses

```
Python: 3.9.5
FastAPI: 0.68
Tortoise-orm: 0.17.8
pytest: 5.2
PostgreSQL: 13.4
```

## Setup

Clone repository

`$ git clone git@github.com:jakub-figat/floppshop-v2`

Then inside root directory run:

`$ make build-dev`

To run application, execute:

`$ make up-dev`

## Tools

`black` and `isort` are used for code formatting

To format, run:

`$ make format`

## Migrations

`aerich` is used for `tortoise-orm` database migrations

To make changes in database after modifying models, run:

`$ make migrations`

To recreate faulty database, use:

`$ make recreate-db` then `$ make aerich-init-db` and `$ make aerich-upgrade`


## Testing

To run tests, execute:

`$ make test`

Tests in specified location:

`$ make test location=tests/test_users`

## Models

When adding new models, register their module in `src.settings.database.DatabaseSettings.APP_MODELS`
in a manner:
```python
APP_MODELS = {
    "app_name": ["src.apps.app_name.models"],
}
```

## SwaggerUI

Swagger docs available at `/api/swagger`
