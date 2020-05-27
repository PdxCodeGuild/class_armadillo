import requests
from flask import Flask, render_template, request
import config
import json, requests
from secrets import api_key

# pete jones helped me with this ! VICTORY
app = Flask(__name__)
app.config['DEBUG'] = True #when left on production

# domain.com/page.html#id
# https://openweathermap.org/current#cities



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city'] # name attribute

        # squirrely brackets - courtesy of Billy
        address = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
        print(f'{address}')
        
        result = requests.get(address)
        
        print(result.text)
        data = result.json()
        print(data['main'])

        y = data['main']['feels_like']
        print(y)

        z = data['weather'][0]['description']
        print(z)

        a = data['name']

        pete = (f'{a} feels like {y}°F and the view has {z}')
        return render_template('weather.html', city=city, result=data['main'], pete=pete)
   
    return render_template('weather.html', city="")



# {'coord': {'lon': -122.68, 'lat': 45.52}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 59.32, 'feels_like': 56.68, 'temp_min': 57, 'temp_max': 61, 'pressure': 1018, 'humidity': 63}, 'visibility': 16093, 'wind': {'speed': 3.36}, 'clouds': {'all': 90}, 'dt': 1589923308, 'sys': {'type': 1, 'id': 5321, 'country': 'US', 'sunrise': 1589891712, 'sunset': 1589945972}, 'timezone': -25200, 'id': 5746545, 'name': 'Portland', 'cod': 200}
