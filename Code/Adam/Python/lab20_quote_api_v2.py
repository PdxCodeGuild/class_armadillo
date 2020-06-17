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


# function prints quots
def get_quotes(page, keyword):
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    # send the request to the api
    response = requests.get(url, headers=headers)
    # declare a dictionary and assign it the json text
    data = json.loads(response.text)
    # print(data)

    # iterate through the data
    for q in data['quotes']:
        last_page = data['last_page']
        # for each iteration assign the value of body to quote
        quote = q['body']
        # and assign the value of author to the variable author
        author = q['author']
        # print quote and author in an f string
        print(f'\n"{quote}" - {author}')


page = 1  # sets the defualt to page to 1
while True:
    # # prompt he user for a keyword
    keyword = input('Enter a keyword to search for quotes: ')
    # # keyword = 'meaning'  # for testing

    # call function to generate quotes
    get_quotes(page, keyword)

    while True:
        # increment the page or break to above while loop
        page_choice = input('Continue to next page? y/n ')
        if page_choice == 'y':  # if yes increment page and generate quotes
            page += 1  # increment the page
            get_quotes(page, keyword)  # call function again
        break
