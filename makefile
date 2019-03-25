venv:
	python3 -m venv venv

update:
	pip install -r requirements.txt

run:
	python3 -m group_generator.generator
