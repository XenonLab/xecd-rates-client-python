
.PHONY: help test package dist dist_test
.DEFAULT: help

VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python3
PIP=${VENV_NAME}/bin/pip
TWINE=${VENV_NAME}/bin/twine

help:
	@echo "make test - Run tests"
	@echo "make package - Builds the package for use or deployment"
	@echo "make dist - Uploads the package to pypi (will ask for credentials)"
	@echo "make dist_test - Uploads the package to test.pypi (will ask for credentials)"

venv: ${VENV_NAME}/bin/activate
${VENV_NAME}/bin/activate: setup.py
	test -d ${VENV_NAME} || python3 -m venv ${VENV_NAME}
	${PIP} install wheel twine
	${PYTHON} setup.py develop
	touch ${VENV_NAME}/bin/activate

test: venv
	${PYTHON} setup.py test

package: venv test
	${PYTHON} setup.py sdist bdist_wheel

dist: package
	${TWINE} upload dist/*

dist_test: package
	${TWINE} upload --repository-url https://test.pypi.org/legacy/ dist/*
