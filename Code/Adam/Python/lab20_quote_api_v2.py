"""
Lab 20 Quote API

Version 2: List Quotes by Keyword

The Favqs Quote API also supports getting a list of quotes associated with a 
given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt
the user for a keyword, list the quotes you get in response, and prompt the 
user to either show the next page or enter a new keyword. You can use string 
concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:

This API endpoint requires an API key be included in a request header. You can 
find documentation of specifying request headers here and documentation on 
authorization with the Favqs API here under "Authorization"

url = 'https://favqs.com/api/quotes?page=1&filter=nature'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)

"""
import requests
import json


while True:
    # prompt he user for a keyword
    keyword = input('Enter a keyword to search for quotes: ')
    # keyword = 'meaning'  # for testing
    page = 1  # sets the defualt to page to 1

    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    # send the request to the api
    response = requests.get(url, headers=headers)
    # declare a dictionary and assign it the json text
    data = json.loads(response.text)
    # print(data)

    # iterate through the data
    number = 1
    for q in data['quotes']:
        # for each iteration assign the value of body to quote
        quote = q['body']
        # and assign the value of author to the variable author
        author = q['author']
        # print quote and author in an f string
        print(f'\n{number}) "{quote}" - {author}')
        number += 1
    
    # last_page = data['last_page']
    # if last_page == ''
    # # while True:

    # # check if on last page; if not on last page, offer user next page option
    # page_input = input('Would you like see the next page? ')

    # # else offer to enter a new keyowrd or to exit



"""
# example of how to reference elements in json

this_dict = [
{"brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color" : ['cherry_red','sky_blue', 'pine_green']
},
{"brand": "VW",
  "model": "Beatle",
  "year": 1972,
  "color" : ['cherry_red','sky_blue', 'pine_green']
},
{"brand": "Buick",
  "model": "Skylar",
  "year": 1968,
  "color" : ['cherry_red','sky_blue', 'pine_green']
}
]
print(this_dict[0]['model'])  # would return Mustang
print(this_dict[1]['color'][1])  # would return sky_blue
"""
