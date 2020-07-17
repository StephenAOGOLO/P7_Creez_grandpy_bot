REM set FLASK_APP=GrandPyBot/controller.py
REM set FLASK_ENV=development
REM set FLASK_RUN_PORT=1000
REM flask run

SET HOME=%CD%
cd .\Scripts
REM cmd /k "cd %HOME%/Scripts&activate&cd %HOME%&set FLASK_APP=GrandPyBot/controller.py&set FLASK_ENV=development&set FLASK_RUN_PORT=1000&flask run"

REM cmd /k "cd %HOME%/Scripts&activate&cd %HOME%"

cmd /k "cd %HOME%/Scripts&activate&cd %HOME%&start_GPB.bat"
