RUN=docker-compose run --rm pageloot


all:
	docker-compose build

run:
	docker-compose up

migrations:
	$(RUN) python3 manage.py makemigrations

migrate:
	$(RUN) python3 manage.py migrate

shell-in:
	docker-compose run --rm pageloot /bin/bash

fmt:
	$(RUN) poetry run black .
	$(RUN) poetry run isort . --profile black

lint:
	$(RUN) poetry run black . --check
	$(RUN) poetry run isort . -c --profile black

test:
	$(RUN) poetry run pytest -x -vvv --pdb

report:
	$(RUN) poetry run pytest -x --pdb

report-fail:
	$(RUN) poetry run pytest --cov-report term --cov-fail-under=90