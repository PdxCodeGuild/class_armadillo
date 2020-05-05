#Lab 20 Quote API Version 2:

"""
For this lab we'll be using the Favqs Quotes API to first get a 
random quote, and then allow the user to find quotes by keyword. To accomplish this 
we'll be using the requests and json libraries. The example below uses a Chuck Norris joke API.

import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url) # send the request to the api
print(response.text) # look at the raw json
data = json.loads(response.text) # turn the json into a python dictionary
print(data['value']) # get a part of the response data out of the dictionary

Version 1: Get a Random Quote
The URL to get a random quote is https://favqs.com/api/qotd, send a request here, 
parse the JSON in the response into a python dictionary, and show the quote and the author.

Version 2: List Quotes by Keyword
The Favqs Quote API also supports getting a list of quotes 
associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
Prompt the user for a keyword, list the quotes you get in response, 
and prompt the user to either show the next page or enter a new keyword. 
You can use string concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:
This API endpoint requires an API key be included in a request header. 
You can find documentation of specifying request headers here and documentation 
on authorization with the Favqs API here under "Authorization".

url = 'https://favqs.com/api/quotes?page=1&filter=nature'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
Other Quote APIs
Programming Quotes
Quotes Garden
get random quote https://quote-garden.herokuapp.com/quotes/random
get quotes by keyword https://quote-garden.herokuapp.com/quotes/search/<keyword/
"""

#Version 2

import string
import requests
import json

# response = requests.get("https://favqs.com/api/qotd")
# json_parse_dict = json.loads(response.text) # parse the JSON in the response into a python dictionary 
# # print(response)
# #print(response.text)
# print(json_parse_dict['quote']['body']) # show the quote which is the body and the author from the dictionary
# print(json_parse_dict ['quote']['author'])

#You can use string concatenation to build the URL.

# create a function below def 
def generate_quotes(page_num, enter_keyword):
    url = f'https://favqs.com/api/quotes?page={page_num}&filter={enter_keyword}' # this Url page_num construction the url putting the page_num and enter_keyword creating a string 
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} # The Authorization
    response = requests.get(url, headers=headers) # you get the json object 
    json_parse_dict = json.loads(response.text) # loading the string turn this json into a dictionary 
    # response = response.text

    # list of dictionary with the quotes and other information like the author and url
    quotes = json_parse_dict["quotes"]
    # print(quotes)
    # create a while loop or for loop to print all 25 quotes for in range..............
    for quote in quotes:
        print(quote["body"])
        # print(quote)

    # print(json_parse_dict["quotes"][0]["body"])
    # print(response.text)

#global variable 
page_num = 1

#Prompt the user for a keyword, list the quotes you get in response,
enter_keyword = input("input the keyword such as (movies, sport, food, places): ")

generate_quotes(page_num, enter_keyword) # calling the function

#and prompt the user to either show the next page or enter a new ke"""yword. 
while True:
    display_next_quotes = input("Would you like display next 25 quotes to play again? ").lower()
    if display_next_quotes in ["yes", "y", "ye", "yeah", "si", "sure"]:
        page_num += 1
        generate_quotes(page_num, enter_keyword) # we call the function again because the user want to play again
    else:
        exit()





