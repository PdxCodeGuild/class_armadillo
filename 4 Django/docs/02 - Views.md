
# Views

**Views** are python functions that are executed when a request follows a route. The view can then respond with HTML, JSON, text, etc. An app's views are contained in its `views.py` file. You can read more about views [here](https://docs.djangoproject.com/en/2.0/topics/http/views/) and [here](https://docs.djangoproject.com/en/2.0/ref/request-response/).


## Requests

The request object received by the view contains lots of important information.

- `request.method` tells you which of the HTTP methods was used (GET, POST, etc)
- `request.body` the raw request body, you can also use `request.read()`
- `request.path` path of the requested page, e.g. `"/music/bands/the_beatles/"`
- `request.GET` dictionary-like object of query parameters
- `request.POST` dictionary-like object of post parameters
- `request.COOKIES` a dictionary of cookies


### Path Parameters

You can specify parameters in the path using a datatype (`int`, `str`) and a name. Those values will then be automatically taken out of the path and passed as parameters to the view function.

##### urls.py
```python
from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    # e.g. /detail/5, /detail/23
    path('detail/<int:todo_item_id>/', views.detail, name='detail')
]
```

##### views.py

```python
def detail(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    return render(request, 'todoapp/detail.html', {'todo_item': todo_item})
```


### Receiving Query Parameters

Query parameters are passed as part of the url and are turned into dictionary-like objects. For example, if the path entered is `/path/to/view/?todo_text=take+a+walk`, we can retrieve the query parameters by name.

```python
def view(request):
    print(request.GET['todo_text']) # 'take a walk'
```


### Receiving a Form Submission

When a form is submitted to a view, the data in the form is arranged into a dictionary. The `name` attributes of the input elements become the `keys` and the values the user enters into the input elements become the `values`. The view can then use the key to get the values out of the dictionary.


```html
<form action="/path/to/receive_form/" method="post">
  <input name="todo_text"/>
  <button type="submit">submit</button>
</form>
```


```python
def receive_form(request):
    print(request.POST['todo_text'])
    return HttpResponse('ok')
```


### Receiving JSON

To read JSON data sent via AJAX, you can use the built-in `json` module to read the request's body. This turns the JSON into a Python dictionary.


```javascript
let data = {foo: 'bar', hello: 'world'}
axios.post('/path/to/postdata', data).then(function(response) {
  console.log(response.data)
})
```

```python
import json
def postdata(request):
    data = json.loads(request.body)
    print(data)
    return HttpResponse('ok')
```


## Responses

### Responding with a String / Raw HTML

```python
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World!')
```

### Responding with a Template

To render a template, use the `render` function. The first parameter is the original request, the second is the location of the template, and the third is a dictionary containing the variables to be rendered.

```python
from django.shortcuts import render
from .models import TodoItem
def index(request):
    todo_items = TodoItem.objects.all()
    context = {'todo_items': todo_items}
    return render(request, 'todos/index.html', context)
```

### Responding with JSON

To respond with a JSON object, you can just pass a dictionary to a JsonResponse.

```python
from django.http import JsonResponse
def getdata(request):
    data = {'foo': 'bar', 'hello': 'world'}
    return JsonResponse(data)
```

```javascript
axios.get('/path/to/getdata/').then(function(response) {
  console.log(response.data)
})
```


### Redirecting

To redirect, you can use the HttpResponseRedirect class. It's also best to use the [reverse](https://docs.djangoproject.com/en/2.2/ref/urlresolvers/#reverse) function to look up the url using the name rather than hard-coding it.

```python
from django.http import HttpResponseRedirect
from django.urls import reverse
def add(request):
    ...
    return HttpResponseRedirect('/todos/')
    return HttpResponseRedirect(reverse('todos:index'))
```

If you need to redirect to a full url, you can use the [redirect](https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#redirect) function.

```python
from django.shortcuts import redirect
def redirect(request):
    return redirect('http://www.mozilla.org/')
```
