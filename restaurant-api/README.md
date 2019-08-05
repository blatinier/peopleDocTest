# restaurant_api
Restaurant API CRUD

## Launch project for dev
Install dependencies:

    docker-compose run --rm server poetry install

Launch:

    docker-compose up

## Run linter

    docker-compose run --rm server poetry run flake8 --exclude=.venv

## Launch tests

    docker-compose run --rm server poetry run nosetests -vv --with-xunit --all-modules --with-coverage --cover-inclusive --cover-xml --cover-xml-file=coverage.xml --cover-package=src
