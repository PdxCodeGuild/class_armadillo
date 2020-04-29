import requests 
import json 


def random_quote():
    url = 'https://favqs.com/api/qotd'
    response = requests.get(url)
    data = json.loads(response.text)
    quote = (data['quote']['body'])
    author = (data['quote']['author'])
    return(f' "{quote}" - {author} ')

print(random_quote())
