.PHONY: help install test run clean

help:
	@echo "Available commands:"
	@echo "  install  - Install dependencies"
	@echo "  test     - Run tests"
	@echo "  run      - Run main application"
	@echo "  clean    - Clean temporary files"

install:
	pip install -r requirements.txt

test:
	python -m pytest test_main.py -v

run:
	python main.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	rm -rf .pytest_cache/ .coverage coverage.xml htmlcov/ 2>/dev/null || true