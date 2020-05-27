from flask import Flask, render_template, request, redirect
import json
import requests

app = Flask('kool_kwotes_api')

# by default views can only receive GET requests
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kotd/') # decorator - path to the view
def qotd(): # view - function that receives the request and returns the response
    response = requests.get('https://favqs.com/api/qotd')
    data = response.json()
    # print(data)
    return render_template('kotd.html', kwote=data['quote']['body'], author=data['quote']['author']) # the response we're returning

'''
# Optional: Flask APIs

Let's build a front-end to an API by sending HTTP requests to the API from our own backend. Check out the [example in the docs](../docs/01%20Flask.md#16-apis).

- **Version 1**: display text/graphics from the API.
- **Version 2**: allow the user to search the API.
- **Version 3**: allow the user to save "favorites" to a `db.json` database.


You can use one of following APIs or [choose your own](https://github.com/public-apis/public-apis).

- Random quote / search quotes: [FavQs](https://favqs.com/api)
- Current weather / forecast: [OpenWeatherMap](https://openweathermap.org/api). You can use the [built-in icons](https://openweathermap.org/weather-conditions#Icon-list) or these [more minimal ones](https://websygen.github.io/owfont/).
- Search books: [Open Library API](https://openlibrary.org/developers/api)
- Search cats: [Cat API](https://docs.thecatapi.com/)
'''









