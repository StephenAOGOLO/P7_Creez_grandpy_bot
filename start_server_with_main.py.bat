SET HOME=%CD%
set FLASK_APP=main.py
set FLASK_ENV=development
set FLASK_RUN_PORT=1000
cd .\Scripts
cmd /k "cd %HOME%/Scripts&activate&cd %HOME%&flask run"
