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


WORKDIR /app

COPY ./pyproject.toml ./poetry.lock .
RUN pip install poetry==$POETRY_VERSION

RUN poetry install --no-ansi --no-interaction

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
