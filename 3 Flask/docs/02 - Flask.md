
# Flask

- [Flask](#flask)
  - [Introduction](#introduction)
  - [Setup](#setup)
  - [Routing](#routing)
  - [Template Rendering](#template-rendering)
  - [Static Files](#static-files)
  - [Forms](#forms)
  - [Query Parameters](#query-parameters)


## Introduction

Flask is a light-weight web application framework written in Python. It performs essentially the same functions as Django, but whereas Django provides many features for you, Flask is bare-bones, and additional features must be installed or developed yourself. While developing your application, your computer will be both the client and the server. When you deploy your application, a dedicated machine will have a public IP address and can send and receive requests from anyone on the web.

## Setup

You can install Flask with `pip install flask`. The [official flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/) provides walkthrough of flask's major features.

Below is a minimal Flask application, it receives a request at `localhost:5000/` and returns a response that simply contains "Hello World!". Copy-paste this code into a file `app.py`.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
```

First, use `cd` to move into the directory that contains the `app.py` file. Then run one of the following commands to set Flask to use that file.

- Linux / MacOS / Bash: `export FLASK_APP=app.py`
- Windows - Command Prompt: `set FLASK_APP=app.py`
- Windows - PowerShell: `$env:FLASK_APP="app.py"`

Next, set Flask to use a development environment, which will restart the server whenever `app.py` changes.

- Linux / MacOS / Bash: `export FLASK_ENV=development`
- Windows - Command Prompt: `set FLASK_ENV=development`
- Windows - PowerShell: `$env:FLASK_ENV="development"`

Finally, you can run the Flask server with `flask run` or `python -m flask run`


## Routing


You can specify multiple different paths

```python
from flask import Flask
app = Flask(__name__)

# localhost:5000
@app.route('/')
def path1():
    return 'you\'re home'

# localhost:5000/path1/
@app.route('/path1/')
def path1():
    return 'you\'re at path 1'

# localhost:5000/path2/
@app.route('/path2/')
def path2():
    return 'you\'re at path 2'

# localhost:5000/path2/path3/
@app.route('/path2/path3/')
def path3():
    return 'you\'re at path 3'
```


You can specify a variable in the path

```python
from flask import Flask
app = Flask(__name__)

# localhost:5000/user/joe/
# localhost:5000/user/jane/
@app.route('/user/<string:username>/')
def show_user_profile(username):
    return f'Showing profile for {username}'

# localhost:5000/user/5/
# localhost:5000/user/656/
@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return f'Showing post with id {post_id}'

```

## Template Rendering

Building HTML with string operations is tedious, so Flask provides a way to use html templates to build data. The templates are html files with special syntax in their own folder which **must** be called `templates`.

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


```python
# localhost:5000?name=joe
@app.route('/')
def index():
    print(request.args['name']) # joe
```


