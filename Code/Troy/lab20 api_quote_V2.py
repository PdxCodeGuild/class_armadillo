# Lab 20 API Quote
# Troy Fitzgerald

'''Version 2: List Quotes by Keyword
The Favqs Quote API also supports getting a list of quotes associated with a 
given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt 
the user for a keyword, list the quotes you get in response, and prompt the user
to either show the next page or enter a new keyword. You can use string concatenation 
to build the URL.'''

# imports the functions.
import json
import requests

# url = 'https://favqs.com/api/quotes?page=1&filter=nature'
# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
# response = requests.get(url, headers=headers)

# requests the url.
requested_url = requests.get('https://favqs.com/api/qotd')
# creates the python dictionary.
requested_data = json.loads(requested_url.text)
# prints the dictionary.
#print(requested_data)


# defines the overall function.
def random_quote_info():
    # asks the user what keyword the user wants to choose.
    user_request = input('What keyword would you like to enter? ')
    # keywords the user has to choose from.
    keyword = ['quote', 'next page', 'author']


    # defines the function to get the quote.
    def get_quote():
        quote_response = requests.get('https://favqs.com/api/qotd')
        return json.loads(quote_response.text)
    #print(get_quote().keys()) - tested for the keys in the dictionary.
    #print(get_quote()['quote']['body'])


    # defines the function to get the author of the quote.    
    def author_response():
        author_response = requests.get('https://favqs.com/api/qotd')
        return json.loads(author_response.text)
    print(author_response()['quote']['author'])

    while True:
        user_answer = input('Would you like to choose another keyword to lookup? ')
        if user_answer in ['y', 'yes']:
            random_quote_info()
        elif user_answer in ['n', 'no']:
            print('Thank you. Goodbye.')
            break
        else: 
            print('Please enter a valid response of yes, y, no, or n!')




    if user_request == 'quote':
        print(get_quote()['quote']['body'])
random_quote_info()


# def next_page():

# def keyword():









