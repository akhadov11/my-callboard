# docker-compose.yml file specified every time since
# docker-compose.override.yml is aim to contain some
# custom overrides that can break the flow
.PHONY: help
.DEFAULT_GOAL := help

timestamp != date -u +"%Y%m%d_%H%M"

image_name = callboard
image_tag = ${image_name}:current
image_dev_tag = ${image_name}-dev:current

requirements = requirements.txt
requirements_dev = requirements-dev.txt

export COMPOSE_INTERACTIVE_NO_CLI=1

help:
	@echo "Help!"

requirements-update:
		@pipenv lock -r > ${requirements} \
			&& echo "Requirements updated (${requirements}).";
		@pipenv lock -r --dev > ${requirements_dev} \
			&& echo "Developemnt requirements updated (${requirements_dev}).";

lint:
	@docker exec callboard-app sh -c '( \
		echo "Running flake8..."; \
		flake8 && echo "flake8 passed." \
		echo "Running pycodestyle..."; \
		pycodestyle && echo "pycodestyle passed."; \
	)'

test:
	@docker exec callboard-app sh -c 'pytest -v'

notebook:
	@python project/manage.py shell_plus --notebook

build-prod-image-raw:
	@docker build . -f ./docker/prod/Dockerfile --tag ${image_tag}

build-image-raw:
	@docker build . -f ./docker/dev/Dockerfile --tag ${image_dev_tag}

build-images-raw: build-image build-prod-image

build-prod-image:
	@docker-compose -f docker-compose.prod.app.yml build --compress --force-rm --no-cache --pull
	@docker-compose -f docker-compose.prod.celery.yml build --compress --force-rm --no-cache --pull

build-image: down
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build --compress --force-rm --no-cache --pull --parallel

celery-purge:
	@docker exec callboard-app sh -c 'celery purge --force --workdir project -A apps.core.celery'

build-images: build-image build-prod-image

up-prod:
	@docker-compose -f docker-compose.prod.app.yml up -d
	@docker-compose -f docker-compose.prod.celery.yml up -d

up-prod-build:
	@docker-compose -f docker-compose.prod.app.yml build --compress --force-rm --no-cache --pull
	@docker-compose -f docker-compose.prod.app.yml up -d --force-recreate
	@docker-compose -f docker-compose.prod.celery.yml build --compress --force-rm --no-cache --pull
	@docker-compose -f docker-compose.prod.celery.yml up -d --force-recreate

up:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

up-build:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build --compress --force-rm --no-cache --pull
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --force-recreate

down-prod:
	@docker-compose -f docker-compose.prod.app.yml down
	@docker-compose -f docker-compose.prod.celery.yml down

down:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

logs:
	@docker logs callboard-app -f --tail 200

logs-celery:
	@docker logs callboard-celery -f --tail 200

exec:
	@docker exec -it callboard-app sh

exec-root:
	@docker exec -u root -it callboard-app sh

exec-db:
	@docker -it exec postgres sh
