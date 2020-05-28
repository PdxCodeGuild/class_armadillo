from flask import Flask, render_template, request, redirect
import json
import requests
from secrets import authorization

app = Flask('kool_kwotes_api')

# # opens database.json, reads the text, turns the json into a python dictionary
# def load_database():
#     with open('database.json', 'r') as file: # open the file
#         text = file.read() # read the text
#     return json.loads(text) # turn the json string into a python dictionary

# # opens database.json, turns the python dictionary into json, and saves it to the file
# def save_database(data):
#     with open('database.json', 'w') as file: # open the file
#         text = json.dumps(data, indent=4) # turn the python dictionary into a json string
#         file.write(text)

# by default views can only receive GET requests
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kotd/') # decorator - path to the view
def qotd(): # view - function that receives the request and returns the response
    response = requests.get('https://favqs.com/api/qotd')
    data = response.json()
    print(data)
    return render_template('kotd.html', kwote=data['quote']['body'], author=data['quote']['author']) # the response we're returning

@app.route('/search/', methods=['POST']) # decorator - path to the view
def search(): # view - function that receives the request and returns the response
    key = request.form['key'].lower().strip() # user input for keyword
    pg = 1 # sets initial page number
    
    while True:
        url = f'https://favqs.com/api/quotes/?filter={key}&page={str(pg)}' # url to API with inputs for keyword and string page number
        # headers = api_key # site requires API key to access list of quotes
        response = requests.get(url, headers=authorization).text # sends request to favqs.com website API for JSON
        kwotes = json.loads(response.text) # creates dictionary from JSON
        if kwotes['quotes'][0]['body'] == 'No quotes found': # checks that key to see if any quotes were found
            message = ''
            kwote = 'Sorry. No kwotes found for that keyword.'
            author = 'Kool Kwotes CEO'
        else: # when quotes were found and exist in dictionary
            message = f'''\n{len(kwotes['quotes'])} kwotes associated with {key} - page {pg}:\n''' # 25 quotes associated with (keywoard) - page 1:
            kwote = kwotes['body']
            author = kwotes['author']
    return render_template('search.html', message=message, kwote=kwote, author=author) # the response we're returning

# @app.route('/enter_task', methods=['POST'])
# def enter_task():
#     # load the database
#     data = load_database()
#     new_text = request.form['new_text']
#     new_pri = request.form['new_pri']
#     task = {
#         'text': new_text,
#         'priority': new_pri,
#     }
#     data['doit'].append(task)

#     save_database(data) # save the data to the database

#     return redirect('/')


'''
# Optional: Flask APIs

Let's build a front-end to an API by sending HTTP requests to the API from our own backend. Check out the [example in the docs](../docs/01%20Flask.md#16-apis).

- **Version 1**: display text/graphics from the API.
- **Version 2**: allow the user to search the API.
- **Version 3**: allow the user to save "favorites" to a `db.json` database.


You can use one of the following APIs or [choose your own](https://github.com/public-apis/public-apis).

- Random quote / search quotes: [FavQs](https://favqs.com/api)
- Current weather / forecast: [OpenWeatherMap](https://openweathermap.org/api). You can use the [built-in icons](https://openweathermap.org/weather-conditions#Icon-list) or these [more minimal ones](https://websygen.github.io/owfont/).
- Search books: [Open Library API](https://openlibrary.org/developers/api)
- Search cats: [Cat API](https://docs.thecatapi.com/)
'''






