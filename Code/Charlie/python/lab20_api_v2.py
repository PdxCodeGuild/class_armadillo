import requests
import json



page = 1

while True:
    key_word = input('Enter a keyword to search for related quotes: ')
    if key_word == '':
        break
    while True:
            
        print(f"Page {page} for search term {key_word}")
        url = f"https://favqs.com/api/quotes?page={page}&filter={key_word}"
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url, headers=headers) # send the request to the api
        data = json.loads(response.text) # turn the json into a python dictionary
        print(data)

        if data['quotes'][0]['body'] == 'No quotes found':
            print('No quotes found')
            break

    
        for quote in data ['quotes']:
            print('"' + quote['body'] + ' - ' + quote['author'])
            print()

        if data['last_page']:
            break
        next_page = input("Would you like to see next page? (y/n) \n")
        if next_page == 'n':
            print('Goodbye')
            break
        elif next_page == 'y':
            continue
        else:
            print('invalid input:')
            return next_page
        page += 1
            # print(get_keyword()['quotes'][0]['body'] + ' - ' + get_keyword()['quotes'][0]['aurthor'])
        