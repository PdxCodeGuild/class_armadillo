import requests 
import json 


def get_quote(page, keyword):
    url =  f"https://favqs.com/api/quotes?page={page}=<page>&filter={keyword}"
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)

    data = json.loads(response.text)

    for i in data['quotes']:
        last_page = data['last_page']
        quote = i['body']
        author = i['author']

        print(f'\n"{quote}" - {author}')

page = 1 
while True:
    keyword = input('enter keyword?: ')
    get_quote(page, keyword)

    while True:
        forward = input('shall we continue? yes or no?')
        if forward == 'yes':
            page += 1
        elif forward == 'no':
            break
