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
describe:
	pwd
test:
	pytest tests
