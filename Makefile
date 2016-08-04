PGPIDENT="fireflyc"
PYTHON=python
PIP=pip
PIP_DOUBAN = -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

all: help

help:
	@echo "dist                 - distribute project."
	@echo "build                - Build project using current python."
	@echo "test                 - Run unittests using current python."
	@echo "clean                - clean"
	@echo "  clean-pyc          - Remove .pyc/__pycache__ files"
	@echo "  clean-build        - Remove setup artifacts."
	@echo "release              - Make PyPI release."

clean: clean-pyc clean-build

release:
	python setup.py register sdist bdist_wheel upload --sign --identity="$(PGPIDENT)"

clean-pyc:
	-find . -type f -a \( -name "*.pyc" -o -name "*$$py.class" \) | xargs rm
	-find . -type d -name "__pycache__" | xargs rm -r

clean-build:
	rm -rf build/ dist/ .eggs/ *.egg-info/

test:
	$(PYTHON) setup.py test

build:
	$(PYTHON) setup.py sdist bdist_wheel

dist_3party:
	mkdir -p dist/thirdparty/pipcache
	$(PIP) download -r requirements.txt -d ./dist/thirdparty/pipcache $(PIP_DOUBAN)
	cp requirements.txt dist/thirdparty/
	echo "pip install --no-index --find-links=pipcache -r requirements.txt">dist/thirdparty/install.sh

dist: clean build dist_3party