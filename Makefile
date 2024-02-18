.PHONY: format lint

setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install black dynaconf
	pip install -e .
format:
	black .
lint:
	black --check .
test:
	pytest tests
