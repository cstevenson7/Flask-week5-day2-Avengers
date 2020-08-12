README
WeekDay2 FLask database

D:\Coding_Temple\week5\day1\Project>python -m venv avengers_env

D:\Coding_Temple\week5\day1\Project>avengers_env\scripts\activate.bat

(fave_five_env) D:\Coding_Temple\week5\day1\Project>pip install flask

set FLASK_APP=app.py

set FLASK_ENV=development

pip install Flask-WTF

pip install email-validator

pip install Flask-SQLAlchemy Flask-Migrate

flask db init

flask db migrate -m "Create User and Post"

flask db upgrade

test
