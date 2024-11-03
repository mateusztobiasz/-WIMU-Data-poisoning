.PHONY: venv black sort mypy flake pylint

venv: 
	poetry env use $(PYTHON_EXEC) && poetry install

black:
	poetry run black .

sort:
	poetry run isort --profile black .

mypy:
	poetry run mypy --disable-error-code=import-untyped .

flake:
	poetry run flake8 --max-line-length 99 .

pylint:
	poetry run pylint .

