SHELL := /bin/bash
PWD := $(shell pwd)

APPNAME:= xecd_rates_client
VERSION := 0.1.0

DOCDIR := ${PWD}/docs
DOCSRCDIR := ${DOCDIR}/source
APPDIR := ${PWD}/${APPNAME}

all: doc build test doc

help:
	@echo -e \
		"${APP_NAME} builder Targets :\n" \
		"  --> build: build project\n" \
		"  --> test: test project\n" \
		"  --> doc: generate documentation\n" \
		"  --> pip: generate pip package\n" \
		"  --> clean: clean project\n" \
		""
build:
	if [ -d ${PWD}/venv ]; then \
		./venv/bin/pip install . ;\
	else \
		python setup.py install ; \
	fi

test:
	if [ -d ${PWD}/venv ]; then \
		./venv/bin/python setup.py test ;\
	else \
		python setup.py test ; \
	fi

initdoc:
	if [ ! -d ${DOCDIR}] ]; then mkdir -p ${DOCDIR}; fi
	if [ ! -f ${DOCSRCDIR}/conf.py ]; then \
		cd ${DOCDIR} && \
		sphinx-quickstart -q -p ${APPNAME} --sep -a ${USER} -v ${VERSION} \
		--ext-autodoc --ext-doctest --ext-coverage --ext-githubpages \
		--ext-viewcode --ext-todo \
		--makefile; \
	fi
	sed -i \
		-e "s/# import os/import os/g" \
		-e "s/# import sys/import sys/g" \
		-e "s/# sys.path.insert(0, os.path.abspath('.'))/sys.path.insert(0, os.path.abspath('..\/..'))/g" \
		-e "s/alabaster/sphinx_rtd_theme/g" ${DOCSRCDIR}/conf.py;
	if ! grep 'README.rst' ${DOCSRCDIR}/index.rst; then \
	sed -i \
		-e "s#Indices and tables#.. include:: ../../README.rst\n\nIndices and tables#g" ${DOCSRCDIR}/index.rst; \
	fi

doc: clean initdoc
	cd ${DOCDIR} && \
	sfood -q ../${APP_NAME} --internal  | sfood-graph | dot -Tsvg > ${DOCSRCDIR}/_static/map.svg && \
	sphinx-apidoc -f -o ${DOCSRCDIR} ${APPDIR} && \
	make -C ${DOCDIR} html


clean:
	if [ -d ${DOCDIR}] ]; then  rm -R ${DOCDIR}/build; fi

.PHONY: all build test doc pip clean