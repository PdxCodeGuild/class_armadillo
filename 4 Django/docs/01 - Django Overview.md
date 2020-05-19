
# Django Overview

- [Django Overview](#django-overview)
  - [What is a web application?](#what-is-a-web-application)
  - [What is Django?](#what-is-django)
  - [Management Commands](#management-commands)
  - [Custom Management Commands](#custom-management-commands)

## What is a web application?

A web application is a website that offers significant functionality beyond simple, static pages. Features include login systems, viewing/saving/editing of information (CRUD), email systems, and many more. [Amazon](http://amazon.com), [LinkedIn](http://linkedin.com), and [Trello](http://trello.com) are all examples of web applications. A web application is split into two major sections: the front-end (client) and the back-end (server).

The **front-end** consists of the HTML, CSS, and JavaScript that runs in the client's browser. HTML represents the structure of your page, CSS describes the presentation and style, and JavaScript allows for interactivity.

The **back-end** consists of code, files, and a database. Unlike the front-end, the code may be in many different languages, depending on which framework is used. The code may be executed in response to HTTP requests by the user or run periodically to perform database operations, testing, etc. Below are some different web application frameworks and the language associated with each.

| Framework | Language |
|--- |--- |
| [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/en/1.1.x/) | Python |
| [Express](https://expressjs.com/) | JavaScript |
| [Spring](https://spring.io/), [Struts](https://struts.apache.org/) | Java |
| [Ruby on Rails](https://rubyonrails.org/) | Ruby |
| [ASP.NET](https://dotnet.microsoft.com/apps/aspnet) | C# |
| [Laravel](https://laravel.com/) | PHP |



## What is Django?

Django is a back-end framework written in Python. Django is a **high-level framework** meaning that it provides a great deal of functionality for you, but you have to connect the pieces together. You have to learn things the 'django way'. This also means that isn't necessarily any deeper intuition behind things, the only answer may be "that's just how Django does things".

For comparison, [Flask](http://flask.pocoo.org/) is also a Python-based back-end framework, but whereas Django is high-level, Flask is low-level, meaning you're only given the most barebones functionality and have to do everything else yourself. Again, it's a balance of convenience and control. You can read more about Django [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django), [here](https://en.wikipedia.org/wiki/Django_(web_framework)), and [here](https://tutorial.djangogirls.org/en/django/).

The core of Django is the [request-response cycle](django_diagram.png). A request is received by the server, it follows a **route**, actives a **view**, which then uses **models** and a **template** to generate a **response**, which is then rendered in the user's browser. The following docs will cover each of these topics in turn, but bear in mind that they're all interdependent.

- Route: a mapping between a URL and a view, uses regex
- View: a Python function which receives a request (url, parameters) and creates a response (html)
- Template: an html file with special syntax for filling in data
- Model: a Python class that parallels a database table

Django applications are contained in a **project** which can have multiple **apps**. How you divide up the functionality of the application is up to your discretion, what's important is that it makes sense to you.


## Management Commands

You can view a full list of the management commands [here](https://docs.djangoproject.com/en/3.0/ref/django-admin/)

| Command | Description |
| ---     | ---         |
| `django-admin startproject myproject` | create a Django project |
| `python manage.py startapp` | create an app |
| `python manage.py runserver` | run the server |
| `python manage.py makemigrations` | stage changes to the database |
| `python manage.py migrate` | apply changes to the database |
| `python manage.py createsuperuser` | create an admin (which has access to the admin panel) |
| `python manage.py collectstatic` | collects static files from each app and puts them into one folder, used for deployment |
| `python manage.py shell` | open an interactive session, often used to do database operations |

## Custom Management Commands

If you need to execute some Python code to perform administrative operations (load data into a database from a file or API, erase saved files, etc), you can write a custom management command. These are executed just like other management commands (`runserver`, `startapp`, `migrate`, etc).

To create a custom management command, first create a `management` folder inside your app. Inside of that, create a `commands` folder. Inside of that, create a `<command name>.py`. Inside your `<command name>.py`, write the following.

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        pass
```

Now you can execute this function using `python manage.py <command name>`. Any parameters you write after the `<command name>` will be passed to the `handle` function.