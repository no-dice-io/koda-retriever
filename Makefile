.PHONY: format lint

setup:
	pip install --upgrade pip
	#pip install -r requirements.txt
	pip install -e .
	pip install pytest
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
	ls -R
	echo "${PYTHONPATH}"
test:
	pytest tests
