SET HOME=%CD%
cd tests
pytest -vvv
cd %HOME%