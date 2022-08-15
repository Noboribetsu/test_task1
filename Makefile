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

deploy:
	git push heroku main

lint:
	poetry run flake8 .

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test task_manager	
	poetry run coverage xml


messages:
	poetry run django-admin makemessages -l ru

compilemessages:
	poetry run django-admin compilemessages 