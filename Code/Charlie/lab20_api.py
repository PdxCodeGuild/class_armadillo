# Lab 20 Quote API
# Version 1


import requests
import json

 


def get_quote():
    url = 'https://favqs.com/api/qotd/'
    response = requests.get(url) # send the request to the api
    data = json.loads(response.text) # turn the json into a python dictionary
    print(data['quote']['author'])
    print(data['quote']['body'])


ask = input("would you like to get a random quote? Enter y for yes or n for no: ")
if ask == 'y':
    get_quote()
        
else:
    print("goodbye")
    
while True:
    again = input("would you like another quote? Enter y for yes n for no: ")
    if again == 'n':
        print("goodbye")
        break
    elif again == 'y':
        get_quote()
    else:
        print("invalid response")
        continue




