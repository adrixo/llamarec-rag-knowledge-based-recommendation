
setup:
	poetry install
	poetry run

run:
	poetry run start

development-env:
	docker compose up