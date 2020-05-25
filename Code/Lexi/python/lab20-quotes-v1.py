# Lab 20 The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

# 1:15 mark of Week 5 > May 4th https://zoom.us/rec/play/tJN_Ie-hr203HdzGuASDUfUvW9S5Kv-shyMX8vYEzk_nB3JXYVOhYOAWY7ZqnZ74BFFAB8zTSaw49UG3?continueMode=true&_x_zm_rtaid=B_eY-b4sRDOhI4C9lZhUUQ.1590447779267.8865d7bf23014c3f1f90087953230acd&_x_zm_rhtaid=568
# sources: https://favqs.com/api/
# other cool ideas: https://www.programmableweb.com/category/keywords/api
import requests
import json 
key = input("What keyword do you want to have a search for quotes by? :")

url = 'https://favqs.com/api/quotes?page=1&filter={key}'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
data = json.loads(response.text)
for quote in data['quotes']:
    print(quote['body'] + ' - ' + quote['author'])

print(data['quote'][0]['body'] + ' - ' + data['quotes'][0]['author'])


# SOURCE: https://www.geeksforgeeks.org/response-json-python-requests/
# import requests
# import json

# response = requests.get('https://favqs.com/api/qotd')

# print(response)

# print(response.json())







# import requests
# import json

# # site we are using
# url = 'https://api.chucknorris.io/jokes/random'
# # send API request
# response = requests.get(url)
# # look at the text in raw JSON format
# print(response.text)
# # create a variable that represents a python dictionary
# # https://www.w3schools.com/python/python_json.asp
# joke = json.loads(response.text)

# print(f'The joke is : "{joke["value"]}".')

# RESULT:
# The joke is : "Chuck Norris can make you evacuate your bowels with a high five.".
