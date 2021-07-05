app_name = boangri/messenger-gunicorn

build:
	@docker build -t $(app_name) .

run:
	docker run --rm --detach -p 5001:5001 $(app_name)

kill:
	@echo 'Killing container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker stop
