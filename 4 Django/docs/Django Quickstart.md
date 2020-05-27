
# Django Quickstart

## 1) Project Setup

1. Create a project: `django-admin startproject blogproj`, if you get 'command not found', try `python -m django startproject blogproj`
2. Move into the project folder `cd blogproj`
3. Create the database with built-in models `python manage.py migrate`
4. Create a superuser `python manage.py createsuperuser`

## 2) App Setup

1. Create an app `python manage.py startapp blogapp`
2. Add `'blogapp'` to the list of `INSTALLED_APPS` in `blogproj/settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'blogapp'
]
```

## 3) Creating a View and a Route

1. In `blogapp/views.py` create an index view

```python
from django.http import HttpResponse

def index(request):
  return HttpResponse('hello world!')
```

2. Create a `blogapp/urls.py` where we'll create a route to get to our view

```python
from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
  path('index/', views.index, name='index')
]
```

3. In `blogproj/urls.py` add a route to our `blogapp/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapp/', include('blogapp.urls'))
]
```

4. Run the server `python manage.py runserver` and in your browser's address bar, type `localhost:8000/blogapp/index/` and you should see `hello world!`



## 4) Render a Template

1. Inside your app folder `blogapp`, create a folder called `templates`. Inside of that, create a folder with the same name as your app `blogapp`. Then inside of that, create your template `index.html`.

```
blogproj
    blogapp
        templates
            blogapp
                index.html
        ...
        admin.py
        models.py
        urls.py
        views.py
    blogproj
        ...
        settings.py
        urls.py
    manage.py
```

2. Inside your `index.html`, put some text to make sure the template is being served by django.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>{{ message }}</h1>
  </body>
</html>
```

3. Change your `blogapp/views.py` to render the template instead of responding with plain text.

```python
from django.shortcuts import render

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'blogapp/index.html', context)
```

4. Go to `localhost:8000/blogapp/index/` and you should see `Hello World!` in an `h1` element.

## 5) Define Your Models

1. In `blogapp/models.py` write your models

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField()
    
    def __str__(self):
        return self.title + ' - ' + self.author
```

2. Run migrations to create the tables from your models
  - `python manage.py makemigrations`
  - `python manage.py migrate`

3. Add your models to your `blogapp/admin.py`

```python
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
```

4. Log into your admin panel `localhost:8000/admin`, you should see your models, and can make sure they work by creating some record

## 6) Render Data in the Template

1. Amend your `blogapp/views.py` to retrieve data from the database and pass it to the template.

```python
from django.shortcuts import render

def index(request):
    blog_posts = BlogPost.objects.order_by('-date_published')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blogapp/index.html', context)
```

2. Use the data to generate HTML inside your template `blogapp/templates/blogapp/index.html`.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <ul>
      {% for blog_post in blog_posts %}
      <li>{{ blog_post.title }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

3. Go to `localhost:8000/blogapp/index` to see the blog posts you entered into the admin panel.


