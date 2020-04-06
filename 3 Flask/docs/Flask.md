
# 1 Flask

## 1.0 Introduction

Flask is a light-weight web application framework written in Python. It performs essentially the same functions as Django, but whereas Django provides many features for you, Flask is bare-bones, and additional features must be installed or developed yourself. You can install Flask with `pip install flask`. The [official flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/) provides walkthrough of flask's major features.

Below is a minimal Flask application, it receives a request at localhost:5000/ and returns a response that simply contains "Hello World!"

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
```

You can run this application by running one the following commands:

- Linux/MacOS: `export FLASK_APP=hello.py`
- Windows / Command Prompt: `C:\path\to\app>set FLASK_APP=hello.py`
- Windows / PowerShell: `C:\path\to\app> $env:FLASK_APP = "hello.py"`

Followed by `flask run` or `python -m flask run`

To set the environment to "development", which will automatically restart the server when any file is changed `export FLASK_ENV=development`

While developing your application, your computer will be bother the client and the server. When you deploy your application, a dedicated machine will have a public IP address and can send and receive requests from anyone on the web.

## 1.1 Routing


You can specify multiple different paths

```python
from flask import Flask
app = Flask(__name__)

@app.route('/path1/')
def path1():
    return 'you\'re at path 1'

@app.route('/path2/')
def path2():
    return 'you\'re at path 2'

@app.route('/path3/')
def path3():
    return 'you\'re at path 3'
```


You can specify variable in the path

```python
from flask import Flask
app = Flask(__name__)

@app.route('/user/<string:username>')
def show_user_profile(username):
    return f'Showing profile for {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Showing post with id {post_id}'

```


## 1.2 Template Rendering

Building HTML with string operations is tedious, so Flask provides a way to use html templates to build data. The templates are html files with special syntax in their own folder which **must** be called `templates`.

#### app.py
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(username):
  name = 'bob'
  temperature = 67
  nums = [1, 2, 3]  
  return render_template('index.html', name=name, temperature=temperature, nums=nums)
```

#### templates/index.html
```html
<p>Hello {{name}}</p>

{% if temperature < 50 %}
<p>cold</p>
{% elif temperature < 80 %}
<p>warm</p>
{% else %}
<p>hot</p>
{% endif %}

<ul>
  {% for num in nums %}
  <li>{{num}}</li>
</ul>
```

## 1.3 Static Files


## 1.4 Forms

By default, routes only respond to GET requests, we can allow them to respond to requests using other methods by passing them to the `route`.


```python

```


## 1.5 Query Parameters


Query parameters can be received by


## 1.6 APIs

Flask applications are just like regular python programs, and can make use of the `requests` library to send HTTP requests to APIs. It's possible to perform these requests when the user accesses a page, and then using the result of that call to render a template. The following example gets a random quote from the `favqs api` and displays it in an html page.


##### random_quote.py
```python
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://favqs.com/api/qotd')
    data = json.loads(response.text)
    quote_author = data['quote']['author']
    quote_text = data['quote']['body']
    return render_template('random_quote.html', quote_author=quote_author, quote_text=quote_text)
```

##### templates/random_quote.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>"{{quote_text}}" - {{quote_author}}</p>
  </body>
</html>
```
