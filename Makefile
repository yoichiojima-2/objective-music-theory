clean:
	-rm poetry.lock
	-find . -name "__pycache__" -type d -print -exec rm -rf {} +
	-find . -name ".pytest_cache" -type d -print -exec rm -rf {} +
	-find . -name ".ruff_cache" -type d -print -exec rm -rf {} +

lint:
	-isort .
	-ruff check --fix .
	-ruff format .

pre-commit: lint clean 

test: 
	pytest -vvv