install:
	poetry install

migrate:
	poetry run python manage.py migrate
	
start:
	poetry run python manage.py runserver 0.0.0.0:8000

setup:
	cp -n .env.example .env
	make install
	make migrate

seed:
	poetry run python manage.py db_seed

deploy:
	git push heroku main

lint:
	poetry run flake8 .

requirements:
	poetry export -o requirements.txt --without-hashes
