.PHONY: format lint

setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install black
	pip install -e .
make re-setup:
	rm -rf .venv
	virtualenv .venv
	. .venv/bin/activate
	make setup
format:
	black .
lint:
	black --check .
describe:
	pwd
test:
	pytest tests
