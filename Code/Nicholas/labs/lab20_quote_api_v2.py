import requests
import json



page = 1
while True:
    keyword = input('Enter a keyword to search for quotes: ') 
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for quotes in data['quotes']: 
        print({quotes['body']})
        print({quotes['author']})
        print({page})
        page_change = input("Would you like to select a new keyword, go to the next page, go back a page, or quit? (enter: new keyword/next page/previous page/done)")
        if page_change == 'new keyword':
            continue
        elif page_change == 'next':
            page += 1
        elif page_change == 'previous':
            page -= 1   
        elif page_change == 'done':
            print('Have a great day!')
            exit()     

