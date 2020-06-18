

# Lab 7: Weather API

Let's use the [OpenWeatherMap API](https://openweathermap.org/api/one-call-api) to display a weather forecast.

## Part 1: Setup

First [make an account](https://openweathermap.org/register), then copy your [api key](https://home.openweathermap.org/api_keys) and put it into a `secrets.js` file in the same directory as your `lab07-weather_api.html`. Make sure `secrets.js` is in the `.gitignore` and then add it to your html file using `<script src="secrets.js"></script>`.


## Part 2: Getting the Weather

The OpenWeatherMap API requires the latitude and longitude to get the weather at a given location. To get the user's current latitude and longitude, we can use the [geolocation api](https://www.w3schools.com/html/html5_geolocation.asp). Another strategy is to use another api to get the user's IP address ([ipify](https://www.ipify.org/), and then another to get the latitude and longitude for the IP address ([ipstack](https://ipstack.com/documentation)).

Once you have the latitude and longitude, you can make the call to [OpenWeatherMap](https://openweathermap.org/api/one-call-api) to get the forecast and display the information in the page.

## Part 3: Using Icons

You can use the [built-in icons](https://openweathermap.org/weather-conditions#Icon-list) or these [more minimal ones](https://websygen.github.io/owfont/).