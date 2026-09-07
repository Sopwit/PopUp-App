.PHONY: help install dev-install run test lint typecheck format build appimage clean check

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
	@echo "  make appimage      - Build a portable Linux AppImage (APP_VERSION required)"
	@echo "  make clean         - Remove temporary files, caches, and build dist"

install:
	$(PYTHON) -m pip install .

dev-install:
	$(PYTHON) -m pip install ".[dev]"

run:
	PYTHONPATH=src $(PYTHON) -m popupapp

test:
	$(PYTEST) -v

lint:
	$(PYTHON) -m compileall src/ tests/

check:
	$(MAKE) lint
	$(MAKE) test

build:
	$(PYTHON) -m PyInstaller --clean packaging/pyinstaller/popupapp.spec

appimage: build
	APP_VERSION=$${APP_VERSION:?Set APP_VERSION, for example 0.1.0} packaging/appimage/build-appimage.sh

clean:
	rm -rf build/ dist/ __pycache__ .pytest_cache/ *.egg-info .eggs/ output/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
