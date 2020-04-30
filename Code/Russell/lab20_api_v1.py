import requests
import json
 

while True:

    url = 'https://favqs.com/api/qotd'
    response = requests.get(url) 
    data = json.loads(response.text)


    quote = data['quote']['body']
    author = data['quote']['author']
    print(quote, '--- ' + author)

    print('Would you like see another quote? Y/N')
    second_quote = input('>').lower()
    if second_quote == 'n':
        print("Have a nice day.")
        break
    elif second_quote == 'y':
        pass







