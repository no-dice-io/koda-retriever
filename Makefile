.PHONY: format lint

setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install black dynaconf
format:
	black .
lint:
	black --check .
test:
	pytest tests
