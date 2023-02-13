SHELL:=/bin/bash
ENV_NAME ?= dev


upgrade-pip:
	pip install --upgrade pip

dependencies:
	pip install -r requirements.txt

docker-dev:
	docker build -t supera ./docker/dev && docker run -d -p 3306:3306 --name supera -e MYSQL_ROOT_PASSWORD=secret supera

docker-tests:
	docker build -t tests_supera ./docker/tests && docker run -d -p 3307:3306 --name tests_supera -e MYSQL_ROOT_PASSWORD=tests tests_supera

unit:
	python -m pytest -s -v

run:
	uvicorn src.run:app --reload 

.PHONY: upgrade-pip, dependencies, envvars, docker-dev, docker-tests, tests, run