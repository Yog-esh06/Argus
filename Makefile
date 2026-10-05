PYTHON ?= python
APP_DIR := backend

.PHONY: install test run backend frontend

install:
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -e .

backend:
	cd $(APP_DIR) && $(PYTHON) -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd frontend && npm install && npm run dev

test:
	pytest

run:
	docker compose up --build
