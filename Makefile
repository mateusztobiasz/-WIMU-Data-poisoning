.PHONY: venv black sort mypy flake pylint

venv: 
	poetry env use $(PYTHON_EXEC)
	poetry install
	
black:
	poetry run black --exclude ./data-poisoning/finetuning/audioldm .

sort:
	poetry run isort --profile black --skip ./wimudp/data-poisoning/finetuning/audioldm .

mypy:
	PYTHONPATH=$(shell pwd)/wimudp/watermarking \
	poetry run mypy --disable-error-code=import-untyped --exclude ./data-poisoning/finetuning/audioldm .

flake:
	poetry run flake8 --max-line-length 120 --exclude ./wimudp/data-poisoning/finetuning/audioldm .

pylint:
	PYTHONPATH=$(shell pwd)/wimudp/watermarking \
	poetry run pylint --ignore=/wimudp/data-poisoning/finetuning/audioldm --max-line-length=120 .

