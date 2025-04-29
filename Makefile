DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d
.PHONY: app-down
app-down:
	${DC} ${APP_FILE} down

.PTHONY:app-shell
app-shell:
	${EXEC} -f ${APP_CONTAINER} bash
