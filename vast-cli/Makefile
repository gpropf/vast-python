
# Follows the steps in https://packaging.python.org/en/latest/tutorials/packaging-projects/

TESTDIR=~/vast-cli-testdir

.PHONY: venv
venv:
	python3 -m venv ./venv


dist: setup.cfg
	rm -rf dist
	python3 -m build

# This target requires that you have a token from the pypi test server in your ~/.pypirc file.
upload-dist-to-test: dist
	python3 -m twine upload --repository testpypi dist/*

.PHONY: test-install
test-install:
	rm -rf $(TESTDIR);
	mkdir $(TESTDIR);
	cp Makefile $(TESTDIR)/
	cd $(TESTDIR); \
	make venv; \
	bash -c "source ./venv/bin/activate; \
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps vast-cli-gpropf"




