PYTHON ?= python3.8

PIP=$(PYTHON) -m pip
PYTEST=$(PYTHON) -m pytest

.PHONY: install-deps
install-deps:
	$(PIP) install -r requirements-dev.txt

.PHONY: test
test:
	$(PYTEST) hijaponmelatele --cov=hijaponmelatele --cov-report=term-missing --cov-fail-under=100 -vv

.PHONY: lint
lint:
	$(PYTHON) -m pylint hijaponmelatele
	$(PYTHON) -m isort hijaponmelatele --check --recursive
	$(PYTHON) -m black hijaponmelatele --check

.PHONY: format
format:
	$(PYTHON) -m isort hijaponmelatele --recursive
	$(PYTHON) -m black hijaponmelatele

.PHONY: runlocal
runlocal:
	$(PYTHON) ./manage.py migrate
	$(PYTHON) ./manage.py runserver
