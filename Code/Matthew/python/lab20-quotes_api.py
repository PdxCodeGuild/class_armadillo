

import requests
import json

# url = 'https://api.chucknorris.io/jokes/random'
# response = requests.get(url) # send the request to the api
# print(response.text) # look at the raw json
# data = json.loads(response.text) # turn the json into a python dictionary
# print(data['value']) # get a part of the response data out of the dictionary
# print(data['url'])


# url = 'https://favqs.com/api/qotd'
# response = requests.get(url)
# # data = response.json()
# data = json.loads(response.text) # turns a json string into a python dictionary
# print(json.dumps(data, indent=4)) # turns a python dictionary into a json string
# print('"' + data['quote']['body'] + '" - ' + data['quote']['author'])


def get_quotes(keyword, page=1):
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}' # our url
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} # our request headers
    response = requests.get(url, headers=headers) # send a request to the api
    data = json.loads(response.text) # turn json string into a python dictionary
    output = []
    for quote in data['quotes']:
        output.append({
            'body': quote['body'],
            'author': quote['author']
        })
    return output

# data = get_quotes('nature')
# print(data)

# data = get_quotes('whale')
# print(data)




page = 1
while True:
    # ask the user for a search term
    keyword = input('Enter a term to search for quotes: ')
    if keyword == '':
        break
    
    while True:
        print(f'Page {page} for search term {keyword}')
        url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}' # our url
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} # our request headers
        response = requests.get(url, headers=headers) # send a request to the api
        data = json.loads(response.text) # turn json string into a python dictionary
        print(data)

        # check if we got any results
        # { ... 'quotes': [{'id': 0, 'favorites_count': 0, 'favorite': False, 'dialogue': False, 'body': 'No quotes found', 'tags': []}]}
        if data['quotes'][0]['body'] == 'No quotes found':
            print('no quotes found')
            break

        # loop over the quotes and print them out
        for quote in data['quotes']:
            print('"' + quote['body'] + '" - ' + quote['author'])
            # print('  tags: ' + ', '.join(quote['tags']))
            print()
        
        # check if we're at the last page
        if data['last_page']:
            break

        # ask the user if they'd like to see the next page
        next_page = input('Would you like to see the next page? (Y/n) ')
        if next_page.lower() == 'n':
            break

        # increment the page
        page += 1
    




