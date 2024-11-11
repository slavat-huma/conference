PYTHON := python3.11
VENV_PATH := .venv


.PHONY: install
install:
	@echo "Installing dependencies from uv.lock"
	@test -d $(VENV_PATH) || $(PYTHON) -m venv $(VENV_PATH)
	@$(VENV_PATH)/bin/pip install -r requirements.txt

run/deps:
	@echo "+ Starting dependencies through docker..."
	@docker compose up -d conference-minio
	@sleep 5

stop/deps:
	@echo "+ Stopping dependencies through docker..."
	@docker compose down
	@sleep 1

server/run:
	@echo "Running the server"
	@python ./main.py
