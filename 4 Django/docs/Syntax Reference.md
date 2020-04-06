

## ORM

| Code                                  | Description          |
|---------------------------------------|----------------------|
| ModelName.objects.all()               | Get all rows         |
| ModelName.objects.filter(field=value) | Get a subset of rows |
| ModelName.objects.get(field=value)    | Get a single row     |
| ModelName.objects.orderby('field')    | Sort rows by field   |
|                                       |                      |
|                                       |                      |
|                                       |                      |


## Common Commands

You can find a complete list of django admin commands [here](https://docs.djangoproject.com/en/2.2/ref/django-admin/).

| Command                                       | Description                      |
|-----------------------------------------------|----------------------------------|
| django-admin startproject \<project name\>    | create a django project          |
| python manage.py startapp \<app name\>        | create an app within the project |
| python manage.py runserver                    | run a django project             |
| python manage.py createsuperuser              | create an admin account          |
| python manage.py changepassword \<user name\> | change a user's password         |
| python manage.py makemigrations               | stage changes to the database    |
| python manage.py migrate                      | apply changes to the database    |


## File Layout

| File/Folder      |                  |                 | explanation                             |
|------------------|------------------|-----------------|-----------------------------------------|
| \<project name\> |                  |                 |  main project folder                    |
|                  | \<project name\> |                 | inner project folder                    |
|                  |                  | \_\_init\_\_.py | defines this folder as a python package |
|                  |                  | settings.py     | project settings                              |
|                  |                  | urls.py         | main routes                                   |
|                  |                  | wsgi.py         | An interface for a web server (Apache, nginx) |
|                  | \<app name\>     |                 |                                         |
|                  |                  | \_\_init\_\_.py | defines this folder as a python package |
|                  |                  | admin.py        | add models to admin panel               |
|                  |                  | apps.py         |                                         |
|                  |                  | models.py       | define your models                      |
|                  |                  | tests.py        |                                         |
|                  |                  | urls.py         |                                         |
|                  |                  | views.py        |                                         |
|                  | manage.py        |                 |                                         |
|                  | db.sqlite3       |                 |                                         |







