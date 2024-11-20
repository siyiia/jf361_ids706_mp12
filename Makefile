install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py test_*.py *.py
format:
	black *.py test_*.py
test:
	pytest --nbval test_*.py
