.PHONY: help install dev-install run test lint typecheck format build clean check

PYTHON ?= python3
PYTEST ?= pytest

help:
	@echo "Super Modern Popup App - Development Targets:"
	@echo "  make install       - Install runtime requirements"
	@echo "  make dev-install   - Install development & build dependencies"
	@echo "  make run           - Launch desktop application"
	@echo "  make test          - Run full test suite with pytest"
	@echo "  make check         - Run syntax, compilation, and test suite"
	@echo "  make build         - Build single-file binary with PyInstaller"
	@echo "  make clean         - Remove temporary files, caches, and build dist"

install:
	$(PYTHON) -m pip install -r install.txt

dev-install:
	$(PYTHON) -m pip install -r dev-install.txt

run:
	PYTHONPATH=src $(PYTHON) popupapp.py

test:
	$(PYTEST) -v

check:
	$(PYTHON) -m compileall src/ tests/ popupapp.py
	$(PYTEST) -v

build:
	$(PYTHON) -m PyInstaller --clean popupapp.spec

clean:
	rm -rf build/ dist/ __pycache__ .pytest_cache/ *.egg-info .eggs/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
