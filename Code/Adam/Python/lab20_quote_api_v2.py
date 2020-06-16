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


# prompt he user for a keyword
keyword = input('Enter a keyword to search for quotes: ')

# sets the defualt to page to 1
page = 1


def find_quotes():
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    print(response)


# list the quotes you get in response
# prompt user to show next page or enter new keyword
