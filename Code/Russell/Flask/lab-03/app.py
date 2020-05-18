from flask import Flask, render_template, request, redirect
import requests
import json


app = Flask(__name__)




@app.route('/', methods=['Get', 'POST'])
def index():

    data = request.form 
    city = data['city']
    country = data['country']
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=vancouver,canada&APPID=')
    weather_data = response.json()
    
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']

    print(description)
    print(temp)
    print(humidity)
    print(wind)
    # print(weather_data)
    return render_template('index.html', city=city, country=country, response=response, temp=temp, humidity=humidity, wind=wind)





# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run