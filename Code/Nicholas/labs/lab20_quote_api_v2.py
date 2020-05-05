# In version 2 of this lab we query an API with a user provided keyword.  
# Quotes associated with the keyword are generated, and the user can either choose
# a new keyword or shift to the next page of quotes.

import requests
import json



page = 1 #start at page 1
keyword = input('Enter a keyword to search for quotes: ') # user input here

url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'  # url with editable sections being page and keyword
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}  #provided authorization token
response = requests.get(url, headers=headers)  #http headers
data = json.loads(response.text)  # loads website from JSON file to python dict
for quotes in data['quotes']: # iterates over quotes on website
    print(f'Quotes associated with "{keyword}": ')
    print(f'''\n"{quotes['body']}"\n''')  # print formated quote pertaining to given keyword
    print(f'''\n-{quotes['author']}\n''')  # corresponding author, formatted
while True:
    page_change = input("Would you like to select a new keyword, go to the next page, previous page, or quit? (enter: new/next/previous/done)")  # loop menu
    if page_change == 'new':  #allows user to enter a new keyword for new search
        keyword = input('Enter a keyword to search for quotes: ') 
        url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        for quotes in data['quotes']: 
            print(f'Quotes associated with "{keyword}": ')
            print(f'''\n"{quotes['body']}"\n''')
            print(f'''\n-{quotes['author']}\n''') 
    elif page_change == 'next':  # prints quotes from next page
        page += 1
        print(f'quotes from page {page}')  # prints quotes from prior page
    elif page_change == 'previous':
        page -= 1  
        print(f'quotes from page {page}')
    elif page_change == 'done':  # for user to leave program
        print('Have a great day!')
        exit()     

