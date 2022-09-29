FROM python:3.10

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install pipenv \
    && apt-get -y install mc

COPY Pipfile.lock Pipfile.lock
COPY alembic.ini alembic.ini

RUN pipenv sync

EXPOSE 8000

CMD pipenv run alembic upgrade head \
    && pipenv run uvicorn web:app --reload --host 0.0.0.0

COPY . /app