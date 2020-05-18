import requests
from flask import Flask, render_template, request
import config
import json
from secrets import api_key


app = Flask(__name__)
app.config['DEBUG'] = True

# domain.com/page.html#id
# https://openweathermap.org/current#cities

@app.route('/')
def index():
    method = 'POST'
    city = request.form['city']
    address = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.api_key}'
    response = requests.get(address, headers = api_key).text
    data = json.loads(response)
    return render_template('weather.html', city=city)



