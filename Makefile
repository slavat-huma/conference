PYTHON := python3.11
VENV_PATH := .venv


.PHONY: install
install:
	@echo "Installing dependencies from uv.lock"
	@test -d $(VENV_PATH) || $(PYTHON) -m venv $(VENV_PATH)
	@$(VENV_PATH)/bin/pip install uv
	@$(VENV_PATH)/bin/uv sync

server/run:
	@echo "Running the server"
	@uv run python ./main.py
