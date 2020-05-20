import requests
import json

read = True
page_number = 0
keyword = input('Enter a keyword to see related quotes: ').lower() # Prompt the user for a keyword

while read:
    page_number += 1
    url = f'https://favqs.com/api/quotes?page={page_number}&filter={keyword}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    quotes_per_page = len(data['quotes'])
    print(f'There are {quotes_per_page} quotes on this page.\n')

    # while loop uses counter to access the index number of each quote and author,
    # then prints the quote and author
    counter = 0
    while counter < quotes_per_page:
        print('   ', data['quotes'][counter]['body'], '---', data['quotes'][counter]['author'], '\n')
        counter += 1

    print('Enter \'next page\' or \'done\'')
    user_option = input('>') 

    
    if user_option == 'done': # if user enters 'done' , variable 'read' becomes false, while loop breaks
        read = False
    elif user_option == 'next page': # if user enters 'next page', loop repeats with incremented page number
        pass
        
