@echo OFF

set LOCAL_ACONDA=C:\Users\cepes\miniconda3\condabin\conda.bat
set LOCAL_PROJECT=C:\xampp\htdocs\alumbratepa
set FLASK_APP=C:\xampp\htdocs\alumbratepa\app\app.py
set FLASK_ENV=development
set FLASK_DEBUG=1

set PYTHONPATH=%LOCAL_PROJECT%;%PYTHONPATH%;%FLASK_APP%;%FLASK_DEBUG%;%FLASK_ENV%
call %LOCAL_ACONDA% activate webapp

call python -m flask run
