FROM python:3.9.5

ENV PYTHONFAULTHANDLER=1 \
PYTHONUNBUFFERED=1 \
PYTHONHASHSEED=random \
# pip
PIP_NO_CACHE_DIR=off \
PIP_DISABLE_PIP_VERSION_CHECK=1 \
# poetry
POETRY_VERSION=1.1.7 \
POETRY_VIRTUALENVS_CREATE=false \
POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update -q && apt-get install -yq netcat

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock .
RUN pip install poetry==$POETRY_VERSION

RUN poetry install --no-ansi --no-interaction

COPY . .

ENTRYPOINT ["sh", "./scripts/start.sh"]

