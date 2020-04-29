# Lab 20 Quote API

import requests
import json

 


a = input("would you like to get a random quote? Enter 'y' for yes or 'n' for no: ")

url = 'https://favqs.com/api/qotd/'
response = requests.get(url) # send the request to the api
# print(response.text) # look at the raw json
data = json.loads(response.text) # turn the json into a python dictionary

# for 
# if a == 'y':
#     print(data)
# elif a == 'n':
#     print('goodbye')
# else:
#     print("invalid response")
#     print(a)

random = data['qotd_date']

print(random)

# print(data) # get a part of the response data out of the dictionary