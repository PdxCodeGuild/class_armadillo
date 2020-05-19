
# Routes

- [Routes](#routes)
  - [Connecting an App's urls.py to a View](#connecting-an-apps-urlspy-to-a-view)
  - [Connecting the Project's urls.py to the App's urls.py](#connecting-the-projects-urlspy-to-the-apps-urlspy)
  - [Parameters in the Path](#parameters-in-the-path)

Routes connect URLs to views. The routes are stored in a **urls.py** file, which can be found in both the project folder and in each of the apps' folders. You can read more about routes [here](https://docs.djangoproject.com/en/2.2/topics/http/urls/). Routes are evaluated **in order**: whichever route matches first is the one used.


## Connecting an App's urls.py to a View

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
]
```


## Connecting the Project's urls.py to the App's urls.py

The `include` function allows you to combine the routes of multiple `urls.py` files into one. This is used to connect the project's 'main' `urls.py` to the `urls.py` in each of the apps.

```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('path/', include('<appname>.urls'))
]
```

## Parameters in the Path

You can specify a parameter in your path using `<type:var_name>`, where `type` is the data type of the parameter (e.g. `str`, `int`, etc). See the [views.md](02%20-%20Views.md#path-parameters) file.
