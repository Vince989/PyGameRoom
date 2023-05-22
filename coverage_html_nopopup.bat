REM python -m pytest . -s .
REM coverage run -m pytest .
pytest

REM coverage report -m
coverage html

del .coverage

pause
