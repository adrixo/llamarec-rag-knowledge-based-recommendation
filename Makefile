
setup:
	poetry install
	poetry shell
	cd dataset
	bash download.sh
	cd ..

run:
	poetry run start

development-env:
	docker compose up