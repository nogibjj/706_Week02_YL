install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C descriptive.py

test:
	python -m pytest -vv --cov=main test_descriptive.py