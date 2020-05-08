import requests
import json

keyword = input('Enter a keyword to search for quotes: ')
page = 1
while True:
    url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
    print(url)
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    data1 = data['quotes']

    for quote in data['quotes']:
        print(quote['body'] + ' - ' + quote['author'])
        print('\n')
    page_choice = input(f"Enter 'next page' or 'done': ")
    if page_choice == 'done':
        exit()
    elif page_choice == 'next page':
        page += 1
        

# print(data1[0]['body'])







# data = {'page': 1, 'last_page': False, 'quotes': [{'id': 0, 'favorites_count': 0, 'favorite': False, 'dialogue': False, 'body': 'No quotes found', 'tags': []}]}
# if data['quotes'][0]['body'] == 'No quotes found':

# data['quotes'][0]['body']

