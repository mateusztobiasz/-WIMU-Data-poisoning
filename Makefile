.PHONY: venv black sort mypy flake pylint

venv: 
	poetry env use $(PYTHON_EXEC) && poetry install

black:
	poetry run black .

sort:
	poetry run isort .

mypy:
	poetry run mypy .

flake:
	poetry run flake8 .

pylint:
	poetry run pylint .

