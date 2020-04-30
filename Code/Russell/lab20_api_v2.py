import requests
import json

# Prompt the user for a keyword, list the quotes you get in response, 
# and prompt the user to either show the next page or enter a new keyword.
# You can use string concatenation to build the URL.


while True:
    keyword = input('Enter a keyword to see related quotes: ').lower()
    page_number = 1
    url = f'https://favqs.com/api/quotes?page={page_number}&filter={keyword}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    quotes_per_page = len(data['quotes'])
    print(f'There are {quotes_per_page} quotes on this page.\n')

    counter = 0
    while counter < len(data['quotes']):
        print('   ', data['quotes'][counter]['body'], '---', data['quotes'][counter]['author'], '\n')
        counter += 1

    print('Enter \'next page\' or \'done\'')
    user_option = input('>')
    if user_option == 'done':
        break
    elif user_option == 'next page':
        page_number += 1


# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes: