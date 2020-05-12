
# Flask

- [Flask](#flask)
  - [Introduction](#introduction)
  - [Routing](#routing)
  - [Template Rendering](#template-rendering)
  - [Static Files](#static-files)
  - [Forms](#forms)
  - [Query Parameters](#query-parameters)
  - [APIs](#apis)


## Introduction

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

## Routing


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


## Template Rendering

Building HTML with string operations is tedious, so Flask provides a way to use html templates to build data. The templates are html files with special syntax in their own folder which **must** be called `templates`.

**app.py**
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

**templates/index.html**
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
  {% endfor %}
</ul>
```

## Static Files

Static files (css, js, images, etc) must be put in a folder called `static`. You can then render the url for them in the template with the code below. Read more about static files in the [official docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/static/).

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}"/>
```

## Forms

Forms allow the user to enter information, below is a simple form with a single text input field. The `action` is the path to which your form will be submitted, the `method` is the http method used, the `input` fields allow the user to enter information and the `name` attribute is used to retrieve that data on the back-end.

```html
<form action="" method="post">
  <input type="text" name="input_text" placeholder="enter some text"/>
  <button type="submit">submit</button>
</form>
```

By default, routes only respond to GET requests, we can allow them to respond to requests using other methods by passing them to the `route`.

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')
```


## Query Parameters


Query parameters can be received in the view using `request.args`

***localhost?name=joe***
```python
def index():
    print(request.args['name']) # joe
```

## APIs

Flask applications are just like regular python programs, and can make use of the `requests` library to send HTTP requests to APIs. It's possible to perform these requests when the user accesses a page, and then using the result of that call to render a template. The following example gets a random quote from the `favqs api` and displays it in an html page.


**random_quote.py**

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


**templates/random_quote.html**

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
