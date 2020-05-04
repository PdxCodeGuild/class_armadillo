import requests 
import json 


def random_quote():
    for i in 
    url = 'https://favqs.com/api/qotd'
    keyword_url = "https://favqs.com/api/quotes?page=<page>&filter=<keyword>"
    response = requests.get(url)
    data = json.loads(response.text)
    quote = (data['quote']['body'])
    author = (data['quote']['author'])
    return(f' "{quote}" - {author} ')

print(random_quote())
