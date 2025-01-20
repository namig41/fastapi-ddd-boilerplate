DC = docker compose
SERVICE_NAME = main-app
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml
CACHE_FILE = docker_compose/cache.yaml
MESSAGE_BROKER_FILE = docker_compose/message_broker.yaml
EXEC = docker exec -it
ENV = --env-file .env

# === APP Section ===
.PHONY: app
app-start:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-drop
app-drop:
	${DC} -f ${APP_FILE} down

.PHONY: logs
app-logs:
	${DC} -f ${APP_FILE} logs -f