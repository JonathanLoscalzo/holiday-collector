# TESTPYPI = https://testpypi.python.org/pypi

install-requirements:
	pip install -r requirements.txt

install:
	pip install .

# develop:
# 	pip install -e .[dev]

uninstall:
	pip uninstall holidaycollector

# # upload:
# # 	python setup.py register
# # 	python setup.py sdist upload

# # test-upload:
# # 	python setup.py register -r $(TESTPYPI)
# # 	python setup.py sdist upload -r $(TESTPYPI)

# # test-install:
# # 	pip install -i $(TESTPYPI) holidaycollector

# # test: develop
# # 	py.test -v --doctest-modules holidaycollector.py test_holidaycollector.py

test: 
	pytest

# .PHONY: install develop uninstall upload test-upload test-install test
