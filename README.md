# Fun and curious


## Installation

### Setup dev environment

1. Install a virtual environment : ```virtualenv .venv```
2. Activate environment : ```.\.venv\Scripts\activate``` (or ```source ./.venv/bin/activate``` under Linux)
3. Install dependencies : ```pip install -r requirements.txt```
4. Install pre-commit : ```pre-commit install```

### Setup database

1. Put the ```.env``` file, which need to be provided by me, in the folder fun_and_curious/settings (inside the project)
2. Check this file regarding your database setup (db user, db port ...)
3. Create a database named fun_and_curious
4. Create tables and users :
   1. Migrate : ```python manage.py migrate```
   2. Create items : ```python manage.py initdata```
   3. Translate items : ```python manage.py translate_data```
   4. Create a superuser for the admin panel : ```python manage.py createsuperuser```


## Utilisation

- Launch the server ```python manage.py runserver```
- You can check the usage of the OpenAPI here : https://app.swaggerhub.com/apis/sadour.mehdi/fun_and_curious/1.0.0#/
- Admin panel : http://127.0.0.1:8000/admin