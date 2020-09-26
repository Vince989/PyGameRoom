REM python -m pytest . -s .
coverage run -m pytest .
REM coverage report -m
coverage html

pause
